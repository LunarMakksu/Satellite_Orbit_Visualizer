import urllib.request
from pathlib import Path

class latest_TLE:

    def get_latest_TLE(fp):
        url ="https://celestrak.org/NORAD/elements/gp.php?CATNR=48924"
        response = urllib.request.urlopen(url)
        lines = response.readlines()
        filepath = fp
        path = Path(f'{filepath}')

        if path.is_file():
             with open (f"{filepath}", 'w') as f:
                f.truncate(0)
                for line in lines:
                    f.writelines(line.decode())
                f.close()

        else:
            with open (f"./{filepath}", 'w') as f:
                for line in lines:
                    f.writelines(line.decode())
                f.close()
        print("Done!")
