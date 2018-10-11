`while ! echo exit | nc localhost 8765; do sleep 1; done; open http://localhost:8765` &
python ../transitfeed/schedule_viewer.py ./data/
