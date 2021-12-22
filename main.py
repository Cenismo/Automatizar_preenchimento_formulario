from selenium import webdriver
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import time


"Escrever código conforme sintax do python"
abrir_navegador = webdriver.Chrome('chromedriver.exe') #Essa etapa é para abrir o navegador. Como colocamos "chrome" ele abrir o chrome.
abrir_navegador.get('https://forms.gle/jzwe8UYCkZkirDPZA') #Essa etapa é para abrir o site desejado

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str("Pablo")) #Colocar nome

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('28.127.603/0001-78')) #Colocar CNPJ

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('BANESTES SA BANCO DO ESTADO DO ESPIRITO SANTO')) #Colocar Razão Social

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')))
elem.send_keys(str('Condomínio do Edifício Palas Center Avenida Princesa Isabel, 574 LOJA A BL.B E LOJA 9 BL.B - Centro, Vitória - ES, 29010-931')) #Colocar Endereço

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('574')) #Colocar Número

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('Centro')) #Colocar Bairro

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('Vitória')) #Colocar Bairro

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('ES')) #Colocar UF

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('29010-931')) #Colocar CEP

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('(27) 3383-1545')) #Colocar telefone

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('pablors.microcamp@gmail.com')) #Colocar email

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('09/08/1995')) #Colocar Vencimento

elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('Vermelho')) #Colocar Descrição
elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[1]/input')))
elem.send_keys(str('1.500,00')) #Colocar Valor



elem = WebDriverWait(abrir_navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
elem.click() #Clicar em enviar

