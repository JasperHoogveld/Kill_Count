import os
import sys
from rich.table import Table
from rich.console import Console

count_file = os.path.join(sys.path[0], 'kill_feed.txt')

def count():
    with open(count_file, 'r') as f:
    # Remove all blank lines
        lines = list(line for line in (l.strip() for l in f) if line)
        res = {}
        for line in lines:
            # Search for playername. Should still integrate a check for amount of quotes
            player = line.split('"')[3]
            # Add totals into a dictionary res
            if any(player in x for x in res):
                for k, v in res.items():
                    if player == k:
                        count = v                
                        count += 1
                        res[player] = count
            else:
                res[player] = 1

    # Sort Descending
    res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))

    # Add result to a table to print
    kill_table = Table(title="Total Kills")
    kill_table.add_column("Player", no_wrap=True, style="cyan")
    kill_table.add_column("Kills", no_wrap=True, style="green", justify='center')
    for k, v in res.items():
        kill_table.add_row(str(k), str(v))

    # Print table in terminal
    console = Console()
    print('')
    return console.print(kill_table)

print(count())

    
