# Atenção -> Executar após a criação do banco com app.py

from services.database import DatabaseManager
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from config import config
from models import *

db_manager = DatabaseManager(config.USER, config.PASSWD, config.HOST, config.PORT, config.DATABASE)
engine = create_engine(db_manager.url)

Session = sessionmaker(bind=engine)
session = Session()

try:
    update_query1 = session.query(User).filter(User.user_id == 3).update({"name": "Charlie Brown Jr."})
    if update_query1:
        print("O nome do usuário de ID 3 foi alterado com sucesso!")
    else:
        raise Exception('Falha na query #1')

    update_query2 = session.query(Hat).filter(Hat.hat_id == 2).update({Hat.price: (130)})
    if update_query2:
        print("O preço foi atualizado para 130 com sucesso!")
    else:
        raise Exception('Falha na query #2')

    update_query3 = session.query(Coupons).filter_by(coupons_id=1).update({"discount": 25})
    if update_query3:
        print("O desconto do cupom de ID = 1 foi alterado para 25%!")
    else:
        raise Exception('Falha na query #3')

    update_query4 = session.query(Hat_Class).filter_by(class_id=1).update({"class_name": "Sniper Elite"})
    if update_query4:
        print("O nome da classe de id = 1 foi atualizado com sucesso!")
    else:
        raise Exception('Falha na query #4')

    update_query5 = session.query(Paint).filter_by(paint_id=3).update({"hex_color": "FF0000"})
    if update_query5:
        print("A cor da pintura com id = 3 foi alterada com sucesso!")
    else:
        raise Exception('Falha na query #5')
    
    session.commit()

except Exception as e:
    print("Ocorreu um erro durante a atualização:", str(e))
    print("Alterações abortadas.")
    session.rollback()

finally:
    session.close()
