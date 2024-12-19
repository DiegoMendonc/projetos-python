CREATE TABLE [dbo].[demanda]
(
  -- Criação da tabela
  id INTEGER PRIMARY KEY,

  data CHAR,

  produto CHAR,

  quantidade INTEGER

-- Vendas de Janeiro
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-01-05', 'Alicate', 10);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-01-10', 'Parafuso', 15);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-01-15', 'Arruela', 20);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-01-20', 'Broca', 25);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-01-25', 'Lixa', 30);

-- Vendas de Fevereiro
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-02-05', 'Alicate', 12);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-02-10', 'Parafuso', 18);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-02-15', 'Arruela', 22);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-02-20', 'Broca', 28);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-02-25', 'Lixa', 35);

-- Vendas de Março
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-03-05', 'Alicate', 14);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-03-10', 'Parafuso', 20);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-03-15', 'Arruela', 24);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-03-20', 'Broca', 30);
INSERT INTO [dbo].[demanda] (data, produto, quantidade) VALUES ('2024-03-25', 'Lixa', 40);
)