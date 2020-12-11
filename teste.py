import pymongo
myclient = pymongo.MongoClient("mongodb+srv://julio:senha@cluster0.pn3vb.mongodb.net/kivyapp?retryWrites=true&w=majority")
db = myclient["kivyapp"]
col_lv = db["lvs"]

lv = {
        "nome_lv": "EBR001",
        "descricao_lv": "A descrição da LV",
        "nome_usuario": "Nome do usuario",
        "email_usuario": "Email do usuario",
        "Data_emissao": "Data de emissão",
        "porcentagem_c": "tantos % de C",
        "quantidade_nc": "Quantidade de NC",
        "quantidade_na": "Quantidade de NA",
        "lv_status": "Status da lista",

        "item1_nome": "Nome do item 1",
        "item1_resultado": "Status item 1 (C, NC, NA)",
        "item1_acao": "Ação item 1",
        "item1_prazo": "Prazo do item 1",
        "item1_responsavel": "Responsável pelo item 1",

        "item2_nome": "Nome do item 2",
        "item2_resultado": "Status item 2 (C, NC, NA)",
        "item2_acao": "Ação item 2",
        "item2_prazo": "Prazo do item 2",
        "item2_responsavel": "Responsável pelo item 2",

        "item3_nome": "Nome do item 3",
        "item3_resultado": "Status item 3 (C, NC, NA)",
        "item3_acao": "Ação item 3",
        "item3_prazo": "Prazo do item 3",
        "item3_responsavel": "Responsável pelo item 3",

        "item4_nome": "Nome do item 4",
        "item4_resultado": "Status item 4 (C, NC, NA)",
        "item4_acao": "Ação item 4",
        "item4_prazo": "Prazo do item 4",
        "item4_responsavel": "Responsável pelo item 4",

        "item5_nome": "Nome do item 5",
        "item5_resultado": "Status item 5 (C, NC, NA)",
        "item5_acao": "Ação item 5",
        "item5_prazo": "Prazo do item 5",
        "item5_responsavel": "Responsável pelo item 5",

        "item6_nome": "Nome do item 6",
        "item6_resultado": "Status item 6 (C, NC, NA)",
        "item6_acao": "Ação item 6",
        "item6_prazo": "Prazo do item 6",
        "item6_responsavel": "Responsável pelo item 6",

        "item7_nome": "Nome do item 7",
        "item7_resultado": "Status item 7 (C, NC, NA)",
        "item7_acao": "Ação item 7",
        "item7_prazo": "Prazo do item 7",
        "item7_responsavel": "Responsável pelo item 7",

        "item8_nome": "Nome do item 8",
        "item8_resultado": "Status item 8 (C, NC, NA)",
        "item8_acao": "Ação item 8",
        "item8_prazo": "Prazo do item 8",
        "item8_responsavel": "Responsável pelo item 8",

        "item9_nome": "Nome do item 9",
        "item9_resultado": "Status item 9 (C, NC, NA)",
        "item9_acao": "Ação item 9",
        "item9_prazo": "Prazo do item 9",
        "item9_responsavel": "Responsável pelo item 9",

    }

col_lv.insert_one(lv)