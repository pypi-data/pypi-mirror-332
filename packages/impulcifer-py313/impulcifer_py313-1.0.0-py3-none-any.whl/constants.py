# -*- coding: utf-8 -*-

from utils import versus_distance

# https://en.wikipedia.org/wiki/Surround_sound
SPEAKER_NAMES = ['FL', 'FR', 'FC', 'BL', 'BR', 'SL', 'SR']

# 파이썬 3.13.2 스타일로 f-string 사용
SPEAKER_PATTERN = f'({"|".join(SPEAKER_NAMES + ["X"])})'
# format() 대신 f-string 사용
SPEAKER_LIST_PATTERN = fr'{SPEAKER_PATTERN}+(,{SPEAKER_PATTERN})*'

SPEAKER_ANGLES = {
    'FL': 30,
    'FR': -30,
    'FC': 0,
    'BL': 150,
    'BR': -150,
    'SL': 90,
    'SR': -90
}

# Speaker delays relative to the nearest speaker
SPEAKER_DELAYS = {
    _speaker: versus_distance(angle=abs(SPEAKER_ANGLES[_speaker]), ear='primary')[1] for _speaker in SPEAKER_NAMES
}
for _speaker in SPEAKER_DELAYS.keys():
    SPEAKER_DELAYS[_speaker] -= min(*SPEAKER_DELAYS.values())

# Each channel, left and right
IR_ORDER = []
# SPL change relative to middle of the head
IR_ROOM_SPL = dict()
for _speaker in SPEAKER_NAMES:
    if _speaker not in IR_ROOM_SPL:
        IR_ROOM_SPL[_speaker] = dict()
    for _side in ['left', 'right']:
        IR_ORDER.append(f'{_speaker}-{_side}')
        IR_ROOM_SPL[_speaker][_side] = versus_distance(
            angle=abs(SPEAKER_ANGLES[_speaker]),
            ear='primary' if _side[0] == _speaker.lower()[1] else 'secondary'
        )[2]

COLORS = {
    'lightblue': '#7db4db',
    'blue': '#1f77b4',
    'pink': '#dd8081',
    'red': '#d62728',
    'lightpurple': '#ecdef9',
    'purple': '#680fb9',
    'green': '#2ca02c'
}

HESUVI_TRACK_ORDER = ['FL-left', 'FL-right', 'SL-left', 'SL-right', 'BL-left', 'BL-right', 'FC-left', 'FR-right',
                      'FR-left', 'SR-right', 'SR-left', 'BR-right', 'BR-left', 'FC-right']

HEXADECAGONAL_TRACK_ORDER = ['FL-left', 'FL-right', 'FR-left', 'FR-right', 'FC-left', 'FC-right', 'LFE-left',
                             'LFE-right', 'BL-left', 'BL-right', 'BR-left', 'BR-right', 'SL-left', 'SL-right',
                             'SR-left', 'SR-right']
