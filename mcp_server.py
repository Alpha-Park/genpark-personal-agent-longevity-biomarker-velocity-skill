# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Longevity Biomarker Velocity Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentLongevityBiomarkerVelocity

mcp = FastMCP("PersonalAgentLongevityBiomarkerVelocity")
client = PersonalAgentLongevityBiomarkerVelocity()

@mcp.tool()
def calculate_phenotypic_age(
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
) -> str:
    """Calculates biological PhenoAge and aging velocity from 9 standard blood panel biomarkers."""
    import json
    return json.dumps(client.calculate_phenotypic_age(
        chronological_age, albumin_g_dl, creatinine_mg_dl, glucose_mg_dl, crp_mg_l,
        lymphocyte_pct, mcv_fl, rdw_pct, alk_phos_u_l, wbc_1000_ul
    ), indent=2)

@mcp.tool()
def prioritize_biomarker_interventions(
    albumin_g_dl: float = 4.5,
    creatinine_mg_dl: float = 0.9,
    glucose_mg_dl: float = 88.0,
    crp_mg_l: float = 0.8,
    lymphocyte_pct: float = 33.0,
    mcv_fl: float = 89.0,
    rdw_pct: float = 12.5,
    alk_phos_u_l: float = 72.0,
    wbc_1000_ul: float = 6.0
) -> str:
    """Ranks biomarker outlier interventions based on biological impact and longevity priority."""
    import json
    return json.dumps(client.prioritize_biomarker_interventions(
        albumin_g_dl, creatinine_mg_dl, glucose_mg_dl, crp_mg_l, lymphocyte_pct,
        mcv_fl, rdw_pct, alk_phos_u_l, wbc_1000_ul
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
