import cv2
import numpy as np
import random

# 파라미터 pass함수
def nothing(x):
    pass

# 그리드를 나눌 변수
gridNum = 0

# 윈도우창 생성
img = cv2.imread('/home/fenor/image/creation.jpg')
dst = cv2.resize(img, (750,750))
cv2.namedWindow('image')
cv2.createTrackbar('grid','image',0,6,nothing)

# 그리드 경계 그리기
def drawGrid(num):
    dst_copy = dst.copy()
    if num > 2: # 퍼즐은 3그리드 이상이 되어야 함
        cell_size = int(750 / num)  # 조각 한 변의 길이는 750px / 나눌 그리드 수
        # 2중 반복문으로 조각별로 경계선을 만들어 줍니다
        for j in range(0, num): 
            x = j * cell_size
            for k in range(0, num):
                y = k * cell_size
                if j == num - 1 and k == num - 1: 
                    cv2.rectangle(dst_copy, (x, y), (x + cell_size, y + cell_size), (255, 255, 255), -1) # 마지막 조각은 흰색으로 지정
                else:
                    cv2.rectangle(dst_copy, (x, y), (x + cell_size, y + cell_size), (0, 0, 255), 1) # 그 외는 외곽선 사각형 그리기
    cv2.imshow('image', dst_copy)

# 그리드 나누기
def sliceGrid(num):
    dst_copy = dst.copy()
    cell_size = int(750 / num) # 한 변의 길이 설정
    varNum_list = [] # 조각을 저장할 변수 선언
    
    # 2중 반복문으로 varNum_list에 조각의 값을 저장합니다
    for i in range(num-1, -1, -1):
        x = i * cell_size
        for j in range(num-1, -1, -1):
            y = j * cell_size
            if i == num - 1 and j == num - 1:
                cv2.rectangle(dst_copy, (x, y), (x + cell_size, y + cell_size), (255, 255, 255), -1)
                varNum_list.append(dst_copy[x: x + cell_size, y: y + cell_size])
            else:
                varNum_list.append(dst_copy[x: x + cell_size, y: y + cell_size])
    return varNum_list

# 풀 수 있는 퍼즐인지 검증
## 검증 1단계 - inversion(역수)계산
def isSolvable(iList):
    invCount = 0
    size = len(iList)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if iList[j] and iList[i] and iList[i] > iList[j]:
                invCount += 1
    return invCount % 2 == 0 # 짝수면 True

## 검증 2단계 - 홀수거리 판단
def moveCount(iList):
    size = len(iList)
    empty_index = iList.index(gridNum*gridNum-1) # 셔플된 퍼즐의 흰 타일 찾기
    target_index = puzzleOK.index(gridNum*gridNum-1) # 완성된 퍼즐의 흰타일 찾기
    return (target_index - empty_index) % 2 == 1 # 홀수면 True

# 인덱스 셔플
def shuffleIndex(iList):
    initialList = iList.copy()  # 초기리스트 저장
    random.shuffle(iList)
    if gridNum % 2 == 1: # 그리드 수가 홀수일 때
        if isSolvable(iList) and moveCount(iList):
            return iList
        else:
            return shuffleIndex(initialList)
    else: # 그리드 수가 짝수일 때
        if isSolvable(iList) == False and moveCount(iList) == False:
            return iList
        else:
            return shuffleIndex(initialList)
        
# 퍼즐 표시
def dispPuzzle(puzzleList, indexList):
    dst_copy = dst.copy()
    cell_size = int(750 / gridNum)
    
    for i in range(gridNum):
        for j in range(gridNum):
            x = i * cell_size
            y = j * cell_size
            dst_copy[x: x + cell_size, y: y + cell_size] = puzzleList[indexList[i * gridNum + j]]
    cv2.imshow('image', dst_copy)
def mouseCallback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼 클릭 시
        cell_size = int(750 / gridNum)
        grid_x = y // cell_size  # 클릭 좌표
        grid_y = x // cell_size  # 클릭 좌표
        
        whitePiece = puzzleOK[gridNum*gridNum-1]  # 하얀색 조각의 번호
        whiteIndex = indexList.index(whitePiece) # 하얀색 조각이 위치한 인덱스
        selectPiece = indexList[grid_x*gridNum + grid_y] # 클릭한 조각의 인덱스
        selectIndex = indexList.index(selectPiece)
        
        white_x = whiteIndex // gridNum
        white_y = whiteIndex % gridNum
        
        if abs(grid_x - white_x) + abs(grid_y - white_y) == 1:
            indexList[whiteIndex] = selectPiece
            indexList[selectIndex] = whitePiece
            
        
# 초기설정 : '트랙바'로 그리드를 설정한 다음 enter를 누르면 퍼즐생성
while True:
    cv2.imshow('image',dst)
    gridNum = cv2.getTrackbarPos('grid','image')
    drawGrid(gridNum)
    if cv2.waitKey(1) & 0xFF == 13 and gridNum > 2:
        break
# 슬라이스한 이미지를 저장
puzzleList = sliceGrid(gridNum)
indexList,puzzleOK,initialList = [],[],[]
for i in range(0,(gridNum*gridNum)):
    indexList.append(i)
    puzzleOK.append(i)
indexList = shuffleIndex(indexList)  # 인덱스 셔플
cv2.setMouseCallback('image', mouseCallback) # 마우스 이벤트 설정
puzzleOK.reverse() # 완성퍼즐
while True:
    dispPuzzle(puzzleList, indexList)
    if np.array_equal(indexList,puzzleOK):
        print("수고하셨습니다")
        break
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()