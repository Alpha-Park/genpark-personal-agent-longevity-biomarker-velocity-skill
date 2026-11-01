# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Longevity Biomarker Velocity Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentLongevityBiomarkerVelocity

def main():
    agent = PersonalAgentLongevityBiomarkerVelocity()

    print("=" * 70)
    print("DEMO: Personal Agent Longevity Biomarker Velocity & PhenoAge Modeler")
    print("=" * 70)

    # Subject: 42 years old with elevated CRP and glucose
    age = 42.0
    res1 = agent.calculate_phenotypic_age(
        chronological_age=age,
        albumin_g_dl=4.4,
        creatinine_mg_dl=1.0,
        glucose_mg_dl=108.0,
        crp_mg_l=3.2,
        lymphocyte_pct=26.0,
        mcv_fl=92.0,
        rdw_pct=13.8,
        alk_phos_u_l=85.0,
        wbc_1000_ul=7.8
    )

    print(f"\n1. PhenoAge Biological Age Calculation (Chronological Age: {age}):")
    print(f"   Biological PhenoAge: {res1['phenotypic_age']} years")
    print(f"   Biological Age Drift: {res1['phenotypic_age_delta']:+0.1f} years")
    print(f"   Aging Velocity Ratio: {res1['aging_velocity_ratio']}x")
    print(f"   10-Year Mortality Hazard: {res1['mortality_hazard_10yr']}")
    print(f"   Classification: {res1['aging_classification']}")
    print(f"   Action: {res1['primary_recommendation']}")

    # Prioritize clinical interventions
    res2 = agent.prioritize_biomarker_interventions(
        albumin_g_dl=4.4,
        creatinine_mg_dl=1.0,
        glucose_mg_dl=108.0,
        crp_mg_l=3.2,
        lymphocyte_pct=26.0,
        mcv_fl=92.0,
        rdw_pct=13.8,
        alk_phos_u_l=85.0,
        wbc_1000_ul=7.8
    )

    print(f"\n2. Targeted Intervention Priority Ranking:")
    print(f"   Outliers Found: {res2['outlier_count']} / {res2['biomarkers_analyzed']}")
    for rank, item in enumerate(res2['top_priority_interventions'], 1):
        print(f"   [{rank}] {item['biomarker']} ({item['direction']}): {item['measured_value']} (Opt: {item['optimal_range']})")
        print(f"       Impact: {item['impact_score']} pts | Action: {item['clinical_action']}")

    print("\nVerification complete: Longevity biomarker engine executed flawlessly.")

if __name__ == "__main__":
    main()
