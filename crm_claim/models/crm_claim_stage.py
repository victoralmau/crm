# -*- coding: utf-8 -*-
from odoo import fields, models


class CrmClaimStage(models.Model):
    """ Model for claim stages. This models the main stages of a claim
        management flow. Main CRM objects (leads, opportunities, project
        issues, ...) will now use only stages, instead of state and stages.
        Stages are for example used to display the kanban view of records.
    """
    _name = "crm.claim.stage"
    _description = "Etapas reclamaciones"
    _order = "sequence"

    name = fields.Char(
        string='Nombre',
        required=True,
        translate=True,
    )
    sequence = fields.Integer(
        default=1,
        help="Usar para ordenar las etapas",
    )    
    case_default = fields.Boolean(
        string='Comun para todos los equipos',
        help="If you check this field, this stage will be proposed by default "
             "on each sales team. It will not assign this stage to existing "
             "teams.")
