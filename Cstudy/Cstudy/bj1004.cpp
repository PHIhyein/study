#include <stdio.h>
#include <math.h>

int main(void) {

	//�� �� �ݺ����� �Է�
	//���2 ����2 �Է¹���
	//�༺ ���� �Է¹޾� �� �� �ݺ����� �Է�
	//����, ������(3) �Է¹���, �ݺ��� ����
	//(�Է� ������ �����ϰ� �ݺ� �� ������ ����ϴ� �ɷ�)
	//���̽� �ϳ� �ݺ� ������, �༺ ���� �ٽ� �Է� ����
	//���̽� �ϳ� ������, �ּ��� ����/��Ż Ƚ�� ���

	//���: �� �� �ϳ��� �༺ ���ο� �־�� ��(and), �� �� �ȿ� �ְų� �ۿ� ������ ���� ����

	int tcase, x1, y1, x2, y2, planet, px, py, r;
	float sqrtr1, sqrtr2;

	scanf_s("%d", &tcase);	//���̽� ���� �Է¹���

	for (int tc = 0; tc < tcase; tc++) {
		scanf_s("%d %d %d %d", &x1, &y1, &x2, &y2);	//���/������ �Է¹���
		scanf_s("%d", &planet);	//�༺ ���� �Է¹���
		int inout = 0; //���� Ƚ�� �ʱ�ȭ

		for (int pn = 0; pn < planet; pn++) {
			scanf_s("%d %d %d", &px, &py, &r);	//�༺ ����, ������ �Է¹���

			sqrtr1 = (px - x1) * (px - x1) + (py - y1) * (py - y1);
			sqrtr2 = (px - x2) * (px - x2) + (py - y2) * (py - y2);
			if (sqrt(sqrtr1) <= r && sqrt(sqrtr2) <= r) {}	//�༺ �ȿ� ���/������ ���� -> ���� ����
			else if(sqrt(sqrtr1) <= r || sqrt(sqrtr2) <= r){
				inout = inout + 1;
			}	//���/������ �� �ϳ��� �༺ �ȿ� ���� -> ���� �߻�
			else {}//���/������ �� �� �༺ �ۿ� ���� -> ���� ����
		}

		printf("%d\n", inout);	//���� Ƚ�� ���
	}

	return 0;
}