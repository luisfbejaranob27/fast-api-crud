from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, CheckConstraint, UniqueConstraint

from app.db.DbConnection import base


class Category(base):
	__tablename__ = "category"

	id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String(100), nullable=False)
	slug = Column(String(120), nullable=False)
	is_active = Column(Boolean, nullable=False, default=False, server_default="False")
	level = Column(Integer, nullable=False, default="100", server_default="100")
	parent_id = Column(Integer, ForeignKey("category.id"), nullable=True)

	__table_args__ = (
		CheckConstraint("LENGTH(name) > 0", name="category_name_length_check"),
		CheckConstraint("LENGTH(slug) > 0", name="category_slug_length_check"),
		UniqueConstraint("name", name="category_name_unique"),
		UniqueConstraint("level", name="category_level_unique"),
		UniqueConstraint("slug", name="uq_category_slug"),
	)
