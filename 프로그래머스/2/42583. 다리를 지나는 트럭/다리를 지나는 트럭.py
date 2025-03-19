# 250319 수 PM 9:27

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리 위 상태 (0: 빈 공간)
    truck_weights = deque(truck_weights)  # 트럭 대기열
    time = 0  # 경과 시간
    current_weight = 0  # 현재 다리 위 트럭 총 무게

    while bridge:
        time += 1
        current_weight -= bridge.popleft()  # 1) 다리에서 트럭 한 대 이동 (제거)

        if truck_weights:  # 2) 새로운 트럭이 다리에 올라갈 수 있는지 확인
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)  # 트럭이 다리로 올라감
                current_weight += truck
            else:
                bridge.append(0)  # 트럭이 올라가지 못하면 빈 공간 유지

    return time  # 3) 모든 트럭이 다리를 지나면 경과 시간 반환