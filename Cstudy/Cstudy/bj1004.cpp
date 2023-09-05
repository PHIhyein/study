#include <stdio.h>
#include <math.h>

int main(void) {

	//몇 번 반복할지 입력
	//출발2 도착2 입력받음
	//행성 개수 입력받아 몇 번 반복할지 입력
	//중점, 반지름(3) 입력받음, 반복할 동안
	//(입력 받은거 저장하고 반복 다 끝나면 출력하는 걸로)
	//케이스 하나 반복 끝내면, 행성 개수 다시 입력 받음
	//케이스 하나 끝내면, 최소의 진입/이탈 횟수 출력

	//계산: 둘 중 하나만 행성 내부에 있어야 함(and), 둘 다 안에 있거나 밖에 있으면 입출 없음

	int tcase, x1, y1, x2, y2, planet, px, py, r;
	float sqrtr1, sqrtr2;

	scanf_s("%d", &tcase);	//케이스 개수 입력받음

	for (int tc = 0; tc < tcase; tc++) {
		scanf_s("%d %d %d %d", &x1, &y1, &x2, &y2);	//출발/도착점 입력받음
		scanf_s("%d", &planet);	//행성 개수 입력받음
		int inout = 0; //입출 횟수 초기화

		for (int pn = 0; pn < planet; pn++) {
			scanf_s("%d %d %d", &px, &py, &r);	//행성 중점, 반지름 입력받음

			sqrtr1 = (px - x1) * (px - x1) + (py - y1) * (py - y1);
			sqrtr2 = (px - x2) * (px - x2) + (py - y2) * (py - y2);
			if (sqrt(sqrtr1) <= r && sqrt(sqrtr2) <= r) {}	//행성 안에 출발/도착점 있음 -> 입출 없음
			else if(sqrt(sqrtr1) <= r || sqrt(sqrtr2) <= r){
				inout = inout + 1;
			}	//출발/도착점 중 하나가 행성 안에 있음 -> 입출 발생
			else {}//출발/도착점 둘 다 행성 밖에 있음 -> 입출 없음
		}

		printf("%d\n", inout);	//입출 횟수 출력
	}

	return 0;
}