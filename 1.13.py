import numpy as np;
m_1 = 5*np.random.random((8,8));
m_2 = 4*np.random.random((8,8));
m_out = np.zeros((8,8));
m_out1 = np.multiply(m_1,m_2);
m_out1 = m_1*m_2;

rows_1 = len(m_1)
cols_1 = len(m_1[0])
rows_2 = len(m_2)
cols_2 = len(m_2[0])

m_out2 = [[0 for row in range(cols_2)] for col in range(rows_1)]

for i in range(rows_1):
    for j in range(cols_2):
        for k in range(cols_1):
            m_out2[i][j] += m_1[i][k] * m_2[k][j]

print(m_out1);
print(m_out2);
