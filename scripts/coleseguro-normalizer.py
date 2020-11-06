import sys
import csv

translations = {
    'es': {
        'Suficientes': 'Suficientes',
        'Poco efectivas': 'Poco efectivas',
        'Insuficientes': 'Insuficientes',
        'Muy insuficientes': 'Muy insuficientes',
        'No lo sé': 'No lo sé',
        'Sí, suficientemente': 'Sí, suficientemente',
        'Sí, aunque no suficientemente': 'Sí, aunque no suficientemente',
        'No me han informado': 'No me han informado',
        'Muy buena': 'Muy buena',
        'Buena': 'Buena',
        'Deficiente': 'Deficiente',
        'Muy deficiente': 'Muy deficiente',
        'Sí': 'Sí',
        'No': 'No',
        'Sí, pero de manera insuficiente': 'Sí, pero de manera insuficiente',
        'Sí, es excelente': 'Sí, es excelente',
        'Sí, es buena': 'Sí, es buena',
        'Es regular': 'Es regular',
        'Es deficiente': 'Es deficiente',
        'Es muy deficiente': 'Es muy deficiente',
        'Sí, pero son insuficientes': 'Sí, pero son insuficientes',
        'Sí, mucho': 'Sí, mucho',
        'Sí, un poco': 'Sí, un poco',
        'Muy poco': 'Muy poco',
        'Nada': 'Nada',
    },
    'gl': {
        'Suficientes': 'Suficientes',
        'Pouco efectivas': 'Poco efectivas',
        'Insuficientes': 'Insuficientes',
        'Moi insuficientes': 'Muy insuficientes',
        'Non o sei': 'No lo sé',
        'Si, suficientemente': 'Sí, suficientemente',
        'Si, aínda que non suficientemente': 'Sí, aunque no suficientemente',
        'Non me informaron': 'No me han informado',
        'Moi boa': 'Muy buena',
        'Boa': 'Buena',
        'Deficiente': 'Deficiente',
        'Moi deficiente': 'Muy deficiente',
        'Si': 'Sí',
        'Non': 'No',
        'Si, pero de maneira insuficiente': 'Sí, pero de manera insuficiente',
        'Si, é excelente': 'Sí, es excelente',
        'Si, é boa': 'Sí, es buena',
        'É regular': 'Es regular',
        'É deficiente': 'Es deficiente',
        'É moi deficiente': 'Es muy deficiente',
        'Si, pero son insuficientes': 'Sí, pero son insuficientes',
        'Si, moito': 'Sí, mucho',
        'Si, un pouco': 'Sí, un poco',
        'Moi pouco': 'Muy poco',
        'Nada': 'Nada',
    },
    'eu': {
        'Nahikoak': 'Suficientes',
        'Eragin gutxikoak': 'Poco efectivas',
        'Urriak': 'Insuficientes',
        'Oso urriak': 'Muy insuficientes',
        'Ez dakit': 'No lo sé',
        'Bai, nahiko': 'Sí, suficientemente',
        'Bai, baina ez nahiko': 'Sí, aunque no suficientemente',
        'Ez naute informatu': 'No me han informado',
        'Oso ona': 'Muy buena',
        'Ona': 'Buena',
        'Txarra': 'Deficiente',
        'Oso txarra': 'Muy deficiente',
        'Bai': 'Sí',
        'Ez': 'No',
        'Bai, baina ez nahiko': 'Sí, pero de manera insuficiente',
        'Bikaina': 'Sí, es excelente',
        'Ona': 'Sí, es buena',
        'Kili-kolo': 'Es regular',
        'Urria': 'Es deficiente',
        'Oso urria': 'Es muy deficiente',
        'Bai, baina ez dira nahiko': 'Sí, pero son insuficientes',
        'Bai, asko': 'Sí, mucho',
        'Bai, pixkat': 'Sí, un poco',
        'Oso gutxi': 'Muy poco',
        'Ezerrez': 'Nada',
    },
    'ca': {
        'Suficients': 'Suficientes',
        'Poc efectives': 'Poco efectivas',
        'Insuficients': 'Insuficientes',
        'Molt insuficients': 'Muy insuficientes',
        'No ho sé': 'No lo sé',
        'Si, suficientment': 'Sí, suficientemente',
        'Si, encara que no prou': 'Sí, aunque no suficientemente',
        'No m\'han informat': 'No me han informado',
        'Molt bona': 'Muy buena',
        'Bona': 'Buena',
        'Deficient': 'Deficiente',
        'Molt deficient': 'Muy deficiente',
        'Si': 'Sí',
        'No': 'No',
        'Si encara que no prou': 'Sí, pero de manera insuficiente',
        'Si, és excel·lent': 'Sí, es excelente',
        'Si, és bona': 'Sí, es buena',
        'És regular': 'Es regular',
        'És deficient': 'Es deficiente',
        'És molt deficient': 'Es muy deficiente',
        'Si però són insuficients': 'Sí, pero son insuficientes',
        'Si, molt': 'Sí, mucho',
        'Si, una mica': 'Sí, un poco',
        'Molt poc': 'Muy poco',
        'Gens': 'Nada',
    },
}

languages = {
    'En castellano': 'es',
    'En galego': 'gl',
    'En euskera': 'eu',
    'En català': 'ca',
}

column_increment = {
    'es': 0,
    'ca': 9,
    'gl': 17,
    'eu': 25,
}

regions = {
    'Almería': 'Andalucía',
    'Cádiz': 'Andalucía',
    'Córdoba': 'Andalucía',
    'Granada': 'Andalucía',
    'Huelva': 'Andalucía',
    'Jaén': 'Andalucía',
    'Málaga': 'Andalucía',
    'Sevilla': 'Andalucía',
    'Huesca': 'Aragón',
    'Teruel': 'Aragón',
    'Zaragoza': 'Aragón',
    'Asturias': 'Principado de Asturias',
    'Islas Baleares': 'Islas Baleares',
    'Las Palmas': 'Canarias',
    'Santa Cruz de Tenerife': 'Canarias',
    'Cantabria': 'Cantabria',
    'Ávila': 'Castilla y León',
    'Burgos': 'Castilla y León',
    'León': 'Castilla y León',
    'Palencia': 'Castilla y León',
    'Salamanca': 'Castilla y León',
    'Segovia': 'Castilla y León',
    'Soria': 'Castilla y León',
    'Valladolid': 'Castilla y León',
    'Zamora': 'Castilla y León',
    'Albacete': 'Castilla-La Mancha',
    'Ciudad Real': 'Castilla-La Mancha',
    'Cuenca': 'Castilla-La Mancha',
    'Guadalajara': 'Castilla-La Mancha',
    'Toledo': 'Castilla-La Mancha',
    'Barcelona': 'Cataluña',
    'Girona': 'Cataluña',
    'Lleida': 'Cataluña',
    'Tarragona': 'Cataluña',
    'Alicante': 'Comunitat Valenciana',
    'Castellón': 'Comunitat Valenciana',
    'Valencia': 'Comunitat Valenciana',
    'Badajoz': 'Extremadura',
    'Cáceres': 'Extremadura',
    'A Coruña': 'Galicia',
    'Lugo': 'Galicia',
    'Ourense': 'Galicia',
    'Pontevedra': 'Galicia',
    'Madrid': 'Comunidad de Madrid',
    'Murcia': 'Murcia',
    'Navarra': 'Navarra',
    'Álava': 'País Vasco',
    'Vizcaya': 'País Vasco',
    'Guipúzcoa': 'País Vasco',
    'La Rioja': 'La Rioja',
    'Ceuta': 'Ceuta',
    'Melilla': 'Melilla',
}

with open(sys.argv[1]) as csv_file:
    with open('output.csv', 'w', newline='') as output:
        csv_writer = csv.writer(output, quoting=csv.QUOTE_ALL)
        csv_reader = csv.reader(csv_file, delimiter=',')
        is_first_row = True

        for row in csv_reader:
            if is_first_row:
                is_first_row = False
                csv_writer.writerow([
                    'id', 'idioma',
                    '¿Sientes que las medidas que se han tomado para garantizar la seguridad en el centro ante el COVID son...?',
                    '¿Sientes que te han informado de las medidas que ha tomado el centro para reducir los riesgos por el COVID?',
                    '¿Cómo calificarías la gestión de los rebrotes en tu centro educativo?',
                    '¿Sabes a quién tienes que contactar en el centro educativo y cómo si hay un positivo?',
                    '¿Consideras que la comunidad educativa (Padres, Madres, Alumnado y Profesorado) han podido participar en las decisiones que se han tomado?',
                    '¿Consideras que la educación digital en tu centro es de calidad? (existencia de equipos adecuados, herramientas adaptadas, metodologías, evaluaciones, etc.)',
                    '¿Sientes que se están tomando medidas para que todos los niños y niñas del centro tengan las mismas oportunidades para seguir con su educación?',
                    '¿Consideras que las medidas que se han tomado pueden impactar negativamente en la salud mental y en el bienestar emocional de los niños y niñas?',
                    'Si hay alguna cuestión sobre la seguridad en los colegios que nos quieras comentar, cuéntanoslo aquí',
                    'centro',
                    'Localidad',
                    'Provincia',
                    'CCAA'
                ])
                continue

            language = languages[row[1]]
            increment = column_increment[language]
            lang_strings = translations[language]

            entry = []
            entry.append(row[0])
            entry.append(row[1])
            for i in range(2 + increment, 11 + increment):
                print(i)
                value = row[i]
                if value == '':
                    entry.append('')
                    continue
                try:
                    translated_value = lang_strings[value]
                except:
                    translated_value = value
                entry.append(translated_value)
            entry.append(row[39])
            location = row[38]
            location_components = location.split(' (')
            municipality = location_components[0]
            province = location_components[1][:-1]
            region = regions[province]
            entry.append(municipality)
            entry.append(province)
            entry.append(region)

            csv_writer.writerow(entry)
