import requests
import csv

files = {
    'Current[id]': (None, 'RCWKCurrent'),
    'RCZCurrent[id]': (None, 'RCZCurrent'),
    'RROE[id]': (None, 'RROE'),
    'RCR[id]': (None, 'RCR'),
    'AFQBalanceCapital[id]': (None, 'AFQBalanceCapital'),
    'RAltmanEMScoreRating[id]': (None, 'RAltmanEMScoreRating'),
    'RPiotroskiFScore[id]': (None, 'RPiotroskiFScore'),
    'Market[id]': (None, 'Market'),
    'Sector[id]': (None, 'Sector'),
    'Trade[id]': (None, 'Trade'),
    'QuoteClose[id]': (None, 'QuoteClose'),
    'QCh12mo[id]': (None, 'QCh12mo'),
    'QCh24mo[id]': (None, 'QCh24mo'),
    'QMin26wCh[id]': (None, 'QMin26wCh'),
    'QMax26wCh[id]': (None, 'QMax26wCh'),
    'QMin52wCh[id]': (None, 'QMin52wCh'),
    'QMax52wCh[id]': (None, 'QMax52wCh'),
    'REVEBITCurrent[id]': (None, 'REVEBITCurrent'),
    'REVEBITDACurrent[id]': (None, 'REVEBITDACurrent'),
}

response = requests.post('https://www.biznesradar.pl/skaner-akcji-get-json/', files=files)
json = response.json()


with open('gpw.csv', 'w', newline='') as csvfile:
    fieldnames = ['Ticker', 'Nazwa', 'Aktualny kurs', 'Rynek', 'Sektor', 'Branża', 'Raport', 'Cena / Wartość księgowa', 'Cena / Zysk', 'ROE', 'Płynność bieżąca', 'Kapitał własny akcjonariuszy jednostki dominującej [tys. PLN]', 'Altman EM-Score', 'Piotroski F-Score', 'Zmiana kursu 12m [%]', 'Zmiana kursu 24m [%]', 'Min 26 tyg. [%]', 'Max 26 tyg. [%]', 'Min 52 tyg. [%]', 'Max 52 tyg. [%]', 'EV / EBIT', 'EV / EBITDA']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')

    writer.writeheader()

    companies = json['data']
    for company in companies:
        writer.writerow({
            'Ticker': company['Symbol']['shortName'],
            'Nazwa': company['Symbol']['mediumName'],
            'Aktualny kurs': company.get('QuoteClose', None),
            'Rynek': company.get('Market', None),
            'Sektor': company.get('Sector', None),
            'Branża': company.get('Trade', None),
            'Raport': company.get('Report', None),
            'Cena / Wartość księgowa': company.get('RCWKCurrent', None),
            'Cena / Zysk': company.get('RCZCurrent', None),
            'ROE': company.get('RROE', None),
            'Płynność bieżąca': company.get('RCR', None),
            'Kapitał własny akcjonariuszy jednostki dominującej [tys. PLN]': company.get('AFQBalanceCapital', None),
            'Altman EM-Score': company.get('RAltmanEMScoreRating', None),
            'Piotroski F-Score': company.get('RPiotroskiFScore', None),
            'Zmiana kursu 12m [%]': company.get('QCh12mo', None),
            'Zmiana kursu 24m [%]': company.get('QCh24mo', None),
            'Min 26 tyg. [%]': company.get('QMin26wCh', None),
            'Max 26 tyg. [%]': company.get('QMax26wCh', None),
            'Min 52 tyg. [%]': company.get('QMin52wCh', None),
            'Max 52 tyg. [%]': company.get('QMax52wCh', None),
            'EV / EBIT': company.get('REVEBITCurrent', None),
            'EV / EBITDA': company.get('REVEBITDACurrent', None),
        })











