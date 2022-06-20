a = [
{'name': 'Confident', 'sentiment': 'Unobserved', 'behaviour': [{'name': 'Confidence', 'comments': None}, {'name': 'Retention', 'comments': None}]},
 {'name': 'Empathetic', 'sentiment': 'Positive', 'behaviour': [{'name': 'Detail', 'comments': [{'id': 1936960211664, 'words': []}, {'id': 1355440997670, 'words': []}, {'id': 5236305195675, 'words': []}]}, {'name': 'Humility', 'comments': None},{'name': 'Confidence', 'comments': None}]},
 {'name': 'Friendly', 'sentiment': 'Positive', 'behaviour': [{'name': 'Intimacy', 'comments': [{'id': 1334755208629, 'words': []}, {'id': 1355440997670, 'words': []}, {'id': 1359879177829, 'words': []}, {'id': 1377517462949, 'words': []}, {'id': 5922633623451, 'words': []}]}, {'name': 'Opening', 'comments': [{'id': 1328454573389, 'words': []}, {'id': 1936960211664, 'words': []}, {'id': 1355440997670, 'words': []}, {'id': 1359879177829, 'words': []}]}, {'name': 'Tone', 'comments': [{'id': 1328454573389, 'words': []}, {'id': 1334755208629, 'words': []}, {'id': 1936960211664, 'words': []}, {'id': 1359879177829, 'words': []}, {'id': 1377517462949, 'words': []}, {'id': 5236305195675, 'words': []}, {'id': 5255056149403, 'words': []}, {'id': 5922633623451, 'words': []}]}]},
 {'name': 'Helpful', 'sentiment': 'Positive', 'behaviour': [{'name': 'Feedback', 'comments': [{'id': 1328454573389, 'words': []}]}, {'name': 'Probing', 'comments': [{'id': 5922633623451, 'words': []}]}, {'name': 'Resolution', 'comments': [{'id': 1334755208629, 'words': []}, {'id': 1355440997670, 'words': []}, {'id': 1359879177829, 'words': []}, {'id': 1377517462949, 'words': []}, {'id': 5236305195675, 'words': []}, {'id': 5922633623451, 'words': []}]}, {'name': 'Servicing', 'comments': None}]},
 {'name': 'Patient', 'sentiment': 'Positive', 'behaviour': [{'name': 'Closing', 'comments': [{'id': 5236305195675, 'words': []}]}, {'name': 'Encouraging', 'comments': [{'id': 1328454573389, 'words': []}, {'id': 1936960211664, 'words': []}, {'id': 1355440997670, 'words': []}, {'id': 5255056149403, 'words': []}, {'id': 5922633623451, 'words': []}]}]},
 {'name': 'Responsive', 'sentiment': 'Positive', 'behaviour': [{'name': 'Follow-up', 'comments': [{'id': 1936960211664, 'words': []}]}, {'name': 'Timing', 'comments': [{'id': 1936960211664, 'words': []}, {'id': 5255056149403, 'words': []}]}]},
 {'name': 'Voice', 'sentiment': 'Positive', 'behaviour': [{'name': 'Conversation', 'comments': [{'id': 1918087332404, 'words': None}]}, {'name': 'Hold', 'comments': [{'id': 1918087332404, 'words': None}]}]}]
 
for dicts in a:
    for key,value in dicts.items():
        if key=='behaviour':
            for j in value.copy():
                if j['comments']==None:
                    value.remove(j)
print(a)
            
