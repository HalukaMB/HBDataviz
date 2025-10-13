import requests

companies = ['Covestro','Fresenius Med Cr','Linde','Puma DE','Hellofresh','Delivery Hero','Beiersdorf','Siemens Energ','Daimler Trk Hldg','Deutsche Wohn','Vitesco Tech Grp','Beiersdorf','Siemens Energ','Wirecard','Lufthansa','Thyssenkrupp','Linde DE','Commerzbank','Prosieben Media','Linde DE','Deutsche Boerse','Uniper','Deutsche Boerse','K&S','Lanxess','Osram Licht','Ceconomy','Man','Deutsche Boerse','Deutsche Boerse','Fresenius','Salzgitter A','Volkswagen','Bayer','Hannover Rueck','Infineon Technol','Postbank','Continent','Hypo Real Hldg','TUI','Altana','Bayer Pharma','UniCredt Bnk','MLP S','TDK Electronics','Evonik Operation','MLP S','Dresdner Bk','Sap','Arcandor','VIAG','Vodafone','Hoechst','Mercedes Benz Gr','Daimler-Benz AG','UniCredt Bnk','GEA Group','Continent','Kaufhof WH','Babcock Borsig','Diebold DE']

API = "https://query1.finance.yahoo.com/v1/finance/search"

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}

results = {}

for name in companies:
    params = {'q': name, 'lang': 'en-US', 'region': 'DE'}
    try:
        r = requests.get(API, params=params, headers=HEADERS, timeout=10)
        data = r.json()
    except Exception:
        # fallback: mark as unknown (site likely returned consent/HTML)
        results[name] = (None, 'error')
        continue

    best = None
    # prefer symbols with .DE or exchange 'GER'
    for item in data.get('quotes', []):
        sym = item.get('symbol')
        exch = item.get('exchange')
        if not sym:
            continue
        if sym.endswith('.DE') or exch == 'GER':
            best = (sym, exch)
            break
        if best is None:
            best = (sym, exch)
    results[name] = best

for k,v in results.items():
    print(k, '->', v)
