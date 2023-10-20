from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager 

from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

from selenium.webdriver.common.by import By


navegador.get("file:///Z:/TI/IDSI/ALUNOS/Gabriel%20Dias/formativa_28.09/custos.html")

navegador.implicitly_wait(3)


dados0 = navegador.find_elements(By.CLASS_NAME, "footer-contact")
dados1 = navegador.find_elements(By.TAG_NAME, "h2")[0].text
dados2 = navegador.find_elements(By.CSS_SELECTOR, "table")[0].text
dados3 = navegador.find_elements(By.ID,"tabela-custos")[0].text
dados4 = navegador.find_elements(By.XPATH, "/html/body/section/table/tbody/tr[8]/td[2]")[0].text
dados5 = navegador.find_elements(By.LINK_TEXT, "Clientes")
dados6 = navegador.find_elements(By.NAME, "Mensagem")

print(dados0)
print(dados1)
print(dados2)
print(dados3)
print(dados4)
print(dados5)
print(dados6)