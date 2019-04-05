#!/usr/bin/env python
# coding: utf-8

# In[1]:
# Não foi feito agosto pois o conceito é o mesmo.

julho = sc.textFile('access_log_Jul95')


# In[2]:


# certifica que é um RDD
type(julho)


# In[3]:


# o primeiro map, por meio de uma função lambda retorna o primeiro elemento do vetor como uma chave, adicionando
# um valor a cada ocorrência
# a função reducesByKey é chamada por meio de uma função lambda que agrupa as chaves somando o número de ocorrência
# do host
hosts_julho = julho.map(lambda host: (host.split(' - - ')[0], 1)).reduceByKey(lambda host, n: host + n)


# In[4]:


# Resposta 1) Total de Hosts únicos
print('Hosts únicos em Julho: %s' % hosts_julho.count())


# In[5]:


# páginas 404
# retorna o resultado de um split por espaço, comparando o segundo elemento do vetor de trás para frente, se é 404
# realiza um map para retornar apenas o nome do site como chave adicionando 1 ao valor
julho_404 = julho.filter(lambda linha: linha.split(' ')[-2] == '404').map(lambda host: (host.split(' - - ')[0], 1))


# In[22]:


# Resposta 2) número de páginas 404
julho_404.count()


# In[20]:


# Filtro para retornar as linhas com erros 404, realizando um map para retornar a url como chave e valor 1
julho_404_top_5  = julho.filter(lambda linha: linha.split(' ')[-2] == '404').map(lambda host: (host.split(' - - ')[0], 1))


# In[23]:

# realizando a redução chave/valor
julho_404_total_top_5 = julho_404_top_5.reduceByKey(lambda host, n: host + n)


# In[25]:


# Resposta 3) 5 URLS que mais causaram erro 404.
julho_404_total_top_5.sortByKey().take(-5)






