from app.schemas.CategorySchema import CategorySchema


def test_category_schema_validation():
	reference = {"name": "Test", "slug": "slug-test"}
	category = CategorySchema(**reference)
	assert category.name == "Test"
	assert category.slug == "slug-test"
