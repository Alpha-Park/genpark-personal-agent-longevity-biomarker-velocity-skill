# -*- coding: utf-8 -*-
"""
Personal Agent Longevity Biomarker Velocity Client
Zero-dependency Levine PhenoAge biological age acceleration modeler, phenotypic aging
velocity calculator, and targeted clinical intervention priority engine.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentLongevityBiomarkerVelocity:
    """
    Quantifies phenotypic aging velocity and projected biological age based on Morgan Levine
    PhenoAge multi-system biomarker regression and clinical mortality hazards.
    """

    def calculate_phenotypic_age(
        self,
        chronological_age: float,
        albumin_g_dl: float = 4.5,
        creatinine_mg_dl: float = 0.9,
        glucose_mg_dl: float = 88.0,
        crp_mg_l: float = 0.8,
        lymphocyte_pct: float = 33.0,
        mcv_fl: float = 89.0,
        rdw_pct: float = 12.5,
        alk_phos_u_l: float = 72.0,
        wbc_1000_ul: float = 6.0
    ) -> Dict[str, Any]:
        """
        Calculates Levine PhenoAge (Biological Age) and aging acceleration rate.
        Linear Predictor xb = -19.907 - 0.0336*Albumin + 0.0095*Creatinine + 0.1953*Glucose
                              + 0.0954*ln(CRP) - 0.0120*Lymphocyte% + 0.0268*MCV + 0.3306*RDW
                              + 0.00188*AlkPhos + 0.0554*WBC + 0.0804*ChronologicalAge
        """
        age = max(18.0, min(110.0, float(chronological_age)))
        alb = max(2.0, min(6.0, float(albumin_g_dl)))
        creat = max(0.4, min(3.5, float(creatinine_mg_dl)))
        glu = max(50.0, min(350.0, float(glucose_mg_dl)))
        crp = max(0.05, min(50.0, float(crp_mg_l)))
        lymph = max(5.0, min(65.0, float(lymphocyte_pct)))
        mcv = max(65.0, min(120.0, float(mcv_fl)))
        rdw = max(9.0, min(25.0, float(rdw_pct)))
        alp = max(20.0, min(300.0, float(alk_phos_u_l)))
        wbc = max(2.0, min(25.0, float(wbc_1000_ul)))

        ln_crp = math.log(crp)

        xb = (
            -19.907
            - 0.0336 * alb
            + 0.0095 * creat
            + 0.1953 * (glu / 10.0) # scaled for standard calibration
            + 0.0954 * ln_crp
            - 0.0120 * lymph
            + 0.0268 * mcv
            + 0.3306 * rdw
            + 0.00188 * alp
            + 0.0554 * wbc
            + 0.0804 * age
        )

        gamma = 0.007692
        exp_xb = math.exp(max(-10.0, min(10.0, xb)))
        integral_term = (math.exp(120.0 * gamma) - 1.0) / gamma
        
        # 10-year cumulative mortality hazard M
        raw_m = 1.0 - math.exp(-exp_xb * integral_term * 0.0001)
        m_hazard = max(0.0001, min(0.9999, raw_m))

        # PhenoAge inverted from Gompertz hazard
        log_term = math.log(-0.00553 * math.log(1.0 - m_hazard))
        pheno_age = round(141.50 + (log_term / 0.090165), 1)
        pheno_age = max(18.0, min(115.0, pheno_age))

        age_delta = round(pheno_age - age, 1)
        velocity_ratio = round(pheno_age / age, 2)

        if age_delta <= -3.0:
            status = "Decelerated Aging (Superior Resilience)"
            action = "Maintain current metabolic, nutritional, and restorative regimen."
        elif age_delta <= 2.0:
            status = "Nominal Aging (Age-Matched Stability)"
            action = "Target identified sub-optimal biomarkers to tip into decelerated aging."
        elif age_delta <= 6.0:
            status = "Accelerated Aging (Elevated Systemic Strain)"
            action = "Implement systemic anti-inflammatory, mitochondrial, and metabolic protocols."
        else:
            status = "Severely Accelerated Aging (High Mortality Risk Gradient)"
            action = "Urgent clinical consultation and targeted pharmacological/lifestyle overhaul."

        return {
            "chronological_age": age,
            "phenotypic_age": pheno_age,
            "phenotypic_age_delta": age_delta,
            "aging_velocity_ratio": velocity_ratio,
            "mortality_hazard_10yr": round(m_hazard, 4),
            "aging_classification": status,
            "primary_recommendation": action
        }

    def prioritize_biomarker_interventions(
        self,
        albumin_g_dl: float = 4.5,
        creatinine_mg_dl: float = 0.9,
        glucose_mg_dl: float = 88.0,
        crp_mg_l: float = 0.8,
        lymphocyte_pct: float = 33.0,
        mcv_fl: float = 89.0,
        rdw_pct: float = 12.5,
        alk_phos_u_l: float = 72.0,
        wbc_1000_ul: float = 6.0
    ) -> Dict[str, Any]:
        """
        Audits individual biomarkers against optimal longevity ranges and calculates
        weighted risk contributions to rank actionable clinical interventions.
        """
        markers = [
            ("CRP (Systemic Inflammation)", crp_mg_l, 0.5, 1.5, "Zone 2 aerobic base, omega-3 EPA/DHA titration, optimize dental/gut microbiome."),
            ("Fasting Glucose (Metabolic Health)", glucose_mg_dl, 75.0, 90.0, "Time-restricted feeding, postprandial ambulation (15-min walk), dietary refined carbohydrate reduction."),
            ("RDW (Red Cell Width / Micro-nutrient)", rdw_pct, 11.5, 13.0, "Screen active folate/B12 methylation, iron ferritin saturation, and sleep fragmentation."),
            ("WBC (Innate Immune Burden)", wbc_1000_ul, 4.0, 6.5, "Identify occult low-grade infections, chronic psychological stress, or excessive overtraining."),
            ("Albumin (Nutritional / Hepatic Synthesis)", albumin_g_dl, 4.4, 5.2, "Ensure adequate high-leucine dietary protein intake (1.6-2.2g/kg), optimize digestive enzymes."),
            ("Creatinine (Renal Clearance / Muscle Index)", creatinine_mg_dl, 0.7, 1.1, "Optimize daily hydration osmolality, monitor glomerular filtration rate (eGFR)."),
            ("Alkaline Phosphatase (Biliary / Bone Turnover)", alk_phos_u_l, 45.0, 80.0, "Evaluate hepatic bile duct drainage, vitamin D/K2 status, and bone mineral density."),
            ("Lymphocyte Percentage (Adaptive Immunity)", lymphocyte_pct, 28.0, 40.0, "Support thymic health, minimize persistent viral reactivation (EBV/CMV)."),
            ("MCV (Erythrocyte Mean Volume)", mcv_fl, 85.0, 93.0, "Evaluate methylation pathways (homocysteine/methylmalonic acid) and alcohol clearance.")
        ]

        scored_issues = []
        for name, val, opt_min, opt_max, intervention in markers:
            val = float(val)
            if val < opt_min:
                deviation = (opt_min - val) / opt_min
                score = round(deviation * 100.0, 1)
                scored_issues.append({
                    "biomarker": name,
                    "measured_value": val,
                    "optimal_range": f"{opt_min} - {opt_max}",
                    "direction": "DEFICIENT",
                    "impact_score": score,
                    "clinical_action": intervention
                })
            elif val > opt_max:
                deviation = (val - opt_max) / opt_max
                score = round(deviation * 100.0, 1)
                scored_issues.append({
                    "biomarker": name,
                    "measured_value": val,
                    "optimal_range": f"{opt_min} - {opt_max}",
                    "direction": "ELEVATED",
                    "impact_score": score,
                    "clinical_action": intervention
                })

        scored_issues.sort(key=lambda x: x["impact_score"], reverse=True)

        return {
            "biomarkers_analyzed": len(markers),
            "outlier_count": len(scored_issues),
            "top_priority_interventions": scored_issues[:4],
            "all_evaluated_outliers": scored_issues
        }
