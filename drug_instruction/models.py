# Python imports
import uuid

# Django imports
from django.db import models

class DrugInstruction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    instruction = models.CharField(max_length=191)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'drug_instruction'