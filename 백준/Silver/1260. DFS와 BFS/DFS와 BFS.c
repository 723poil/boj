#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 10000
#define TRUE 1

typedef struct _node* nodePointer;
typedef struct _node {
	int vertex;
	nodePointer link;
} node;

nodePointer vertices[MAX_SIZE];
short int visited[MAX_SIZE];
nodePointer front, rear;

int N, M, V;

void insert(int v1, int v2);
nodePointer sorted(nodePointer x);
void dfs(int v);
void bfs(int v);
void addq(int vertex);
int deleteq();

int main(void) {

	scanf("%d %d %d", &N, &M, &V);

	for (int i = 0; i < M; i++) {
		int v1, v2;
		scanf("%d %d", &v1, &v2);
		insert(v1, v2);
		insert(v2, v1);
	}

	for (int i = 1; i <= N; i++) {
		if (!vertices[i]) continue;
		vertices[i] = sorted(vertices[i]);
	}

	dfs(V);
	printf("\n");
	for (int i = 1; i <= N; i++) {
		if (!vertices[i]) continue;
		visited[i] = 0;
	}

	bfs(V);

	return 0;
}

void insert(int v1, int v2) {
	nodePointer node = (nodePointer)malloc(sizeof(node));
	node->vertex = v2;
	node->link = NULL;
	if (!vertices[v1]) {
		vertices[v1] = node;
		return;
	}
	nodePointer temp = vertices[v1];
	for (;temp->link != NULL;temp = temp->link);
	temp->link = node;
}

nodePointer sorted(nodePointer x) {
	if (x->link == NULL) {
		return x;
	}
	nodePointer temp1, temp2;
	temp1 = x;
	while (temp1) {
		for (temp2 = temp1; temp2; temp2 = temp2->link) {
			if (temp2->vertex < temp1->vertex) {
				int temp = temp1->vertex;
				temp1->vertex = temp2->vertex;
				temp2->vertex = temp;
			}
		}
		temp1 = temp1->link;
	}
	
	return x;
}

void dfs(int v) {
	nodePointer w;
	visited[v] = TRUE;
	printf("%d ", v);
	for (w = vertices[v]; w; w = w->link) {
		if (!visited[w->vertex]) {
			dfs(w->vertex);
		}
	}
}

void bfs(int v) {
	nodePointer w;
	front = rear = NULL;
	printf("%d ", v);
	visited[v] = TRUE;

	addq(v);
	while (front) {
		v = deleteq();
		for (w = vertices[v]; w; w = w->link) {
			if (!visited[w->vertex]) {
				printf("%d ", w->vertex);
				addq(w->vertex);
				visited[w->vertex] = TRUE;
			}
		}
	}
}

void addq(int vertex) {
	nodePointer node = (nodePointer)malloc(sizeof(node));
	node->vertex = vertex;
	node->link = NULL;
	if (!front) {
		front = node;
	}
	else {
		rear->link = node;
	}
	rear = node;
}

int deleteq() {
	if (!front) {
		return -9999;
	}
	nodePointer node = front;
	int item = front->vertex;
	
	front = node->link;

	return item;
}