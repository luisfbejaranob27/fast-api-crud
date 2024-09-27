from typing import Annotated, Optional

from pydantic import BaseModel, constr


class CategorySchema(BaseModel):
	name: Annotated[str, constr(min_length=1)]
	slug: Annotated[str, constr(min_length=1)]
	is_active: Optional[bool] = False
	level: Optional[int] = 100
	parent_id: Optional[int] = None
