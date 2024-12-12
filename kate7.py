from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Создаём базу данных
engine = create_engine("postgresql+psycopg2://cat:1@localhost/money")

# Базовый класс для всех моделей
Base = declarative_base()

# Определяем модель Category
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Связь с таблицей Product
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"

# Определяем модель Product
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Связь с таблицей Category
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category_id={self.category_id})"

# Создаём таблицы в базе данных
Base.metadata.create_all(engine)

# Создаём сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# CRUD-операции

# 1. Создание категории
def create_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Категория создана: {category}")
    return category

# 2. Создание продукта
def create_product(name, price, category_id):
    product = Product(name=name, price=price, category_id=category_id)
    session.add(product)
    session.commit()
    print(f"Продукт создан: {product}")
    return product

# 3. Чтение продуктов по категории
def get_products_by_category(category_id):
    category = session.query(Category).filter_by(id=category_id).first()
    print(f"Продукт в категории '{category.name}':")
    for product in category.products:
        print(product)

# 4. Обновление категории у продукта
def update_product_category(product_id, new_category_id):
    product = session.query(Product).filter_by(id=product_id).first()
    product.category_id = new_category_id
    session.commit()
    print(f"Продукт обновлен: {product}")

# 5. Удаление категории и всех связанных продуктов
def delete_category(category_id):
    category = session.query(Category).filter_by(id=category_id).first()
    session.delete(category)
    session.commit()
    print(f"Категория удалена: {category}")

# Пример использования
if __name__ == "__main__":
    # Создаём категории
    category1 = create_category("Игрушки")
    category2 = create_category("Машины")

    # Создаём продукты
    product1 = create_product("Кукла", 10000, category1.id)
    product2 = create_product("Матрешка", 500, category1.id)
    product3 = create_product("Ауди", 2000000, category2.id)

    # Чтение продуктов по категории
    get_products_by_category(category1.id)
    get_products_by_category(category2.id)

    # Обновление категории у продукта
    update_product_category(product3.id, category1.id)

    # Удаление категории и всех связанных продуктов
    delete_category(category1.id)