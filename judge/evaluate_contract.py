#!/usr/bin/env python3
"""Evaluation-time contract helper. Semantic verdicts come only from an LLM judge."""
import json

def judge_input(task, golden, returned_memory_context):
    return {"task_id":task["task_id"],"task_text":task["task_text"],"issue_timestamp":task["issue_timestamp"],"requester_id":task["requester_id"],"requester_type":task["requester_type"],"returned_memory_context":returned_memory_context,"required_memory":golden["required_memory"],"one_of_groups":golden["one_of_groups"],"required_provenance":golden["required_provenance"],"forbidden_as_current":golden["forbidden_as_current"],"forbidden_to_return":golden["forbidden_to_return"],"expected_retrieval_mode":golden["expected_retrieval_mode"],"useful_but_optional":golden["useful_but_optional"]}

def final_verdict(llm_semantic_verdict, returned_token_count, max_output_tokens):
    # Deliberately the only programmatic pass/fail check.
    budget_compliant = returned_token_count <= max_output_tokens
    return {"semantic_pass":bool(llm_semantic_verdict["semantic_pass"]),"budget_compliant":budget_compliant,"final_pass":bool(llm_semantic_verdict["semantic_pass"] and budget_compliant)}

def aggregate(results, tasks):
    by_task={t["task_id"]:t for t in tasks}
    def rate(rows,key="final_pass"):
        return None if not rows else sum(bool(x[key]) for x in rows)/len(rows)
    categories={str(c):rate([r for r in results if by_task[r["task_id"]]["primary_category"]==c]) for c in range(1,11)}
    dims=sorted({d for t in tasks for d in t["dimension_labels"]})
    dimensions={d:rate([r for r in results if d in by_task[r["task_id"]]["dimension_labels"]]) for d in dims}
    concept_rows=[c for r in results for c in r["semantic_verdict"]["required_concepts"]]
    for r in results:
        for g in r["semantic_verdict"]["one_of_groups"]:
            selected=g.get("satisfied_by_alternative_id")
            chosen=next((a for a in g["alternatives"] if a["alternative_id"]==selected),None)
            if chosen is not None:concept_rows.extend(chosen["concepts"])
    prov=[p for r in results for p in r["semantic_verdict"]["provenance_checks"]]
    flags=[r["semantic_verdict"]["error_flags"] for r in results]
    set_rows=[r for r in results if "set_completeness" in by_task[r["task_id"]]["dimension_labels"]]
    conf_rows=[r for r in results if r["semantic_verdict"]["forbidden_to_return_checks"]]
    contamination_types=["irrelevant","stale-as-current","unauthorized","incorrect","wrong-entity","extra-set-member"]
    contamination_by_type={k:(None if not results else sum(any(x["type"]==k for x in r["semantic_verdict"]["contamination"]) for r in results)/len(results)) for k in contamination_types}
    return {"overall_pass_rate":rate(results),"category_pass_rates":categories,"dimension_pass_rates":dimensions,"required_concept_coverage":None if not concept_rows else sum(c["satisfies_requirement"] for c in concept_rows)/len(concept_rows),"contamination_rate":None if not results else sum(bool(r["semantic_verdict"]["contamination"]) for r in results)/len(results),"contamination_by_type":contamination_by_type,"provenance_correctness":None if not prov else sum(p["satisfied"] for p in prov)/len(prov),"unsupported_fabrication_rate":None if not flags else sum(x["unsupported_fabrication"] for x in flags)/len(flags),"confidentiality_violation_rate":None if not conf_rows else sum(r["semantic_verdict"]["error_flags"]["confidentiality_leak"] for r in conf_rows)/len(conf_rows),"set_completeness_rate":rate(set_rows),"budget_compliance_rate":rate(results,"budget_compliant")}
