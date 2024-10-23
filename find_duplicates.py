import pandas as pd

# Función para encontrar duplicados
def find_duplicates(contacts):
    matches = []
    
    for i, contact1 in contacts.iterrows():
        for j, contact2 in contacts.iterrows():
            if i >= j:  # Evitar comparaciones repetidas
                continue
            
            score = 0
            # Comparar correos electrónicos
            if contact1['email'] == contact2['email']:
                score += 2
            
            # Comparar nombres y apellidos
            if contact1['name'] == contact2['name'] and contact1['name1'] == contact2['name1']:
                score += 3
            
            # Comparar códigos postales
            if contact1['postalZip'] == contact2['postalZip']:
                score += 1
            
            # Comparar direcciones
            if contact1['address'] == contact2['address']:
                score += 1
            
            # Determinar la precisión de la coincidencia
            if score >= 5:
                accuracy = 'High'
            elif score >= 3:
                accuracy = 'Medium'
            elif score > 0:
                accuracy = 'Low'
            else:
                continue
            
            matches.append({
                'ContactID Source': contact1['contactID'],
                'ContactID Match': contact2['contactID'],
                'Match Accuracy': accuracy
            })
    
    return pd.DataFrame(matches)

# Leer el archivo CSV
contacts_df = pd.read_csv('contacts.csv', delimiter=';')

# Encontrar duplicados
duplicates_df = find_duplicates(contacts_df)

# Mostrar resultados
print(duplicates_df)
