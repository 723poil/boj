#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 10001

typedef struct _Tree* treePointer;
typedef struct _Tree {
	int key;
	treePointer leftChild;
	treePointer rightChild;
} Tree;

treePointer root;

int treeNodeKey[MAX_SIZE];

void insertion(int k);
treePointer modifiedSearch(treePointer node, int k);
void postorder(treePointer cur);

int main(void) {
	
	int i = 0;
	while (scanf("%d", &treeNodeKey[i++])) {
		if (treeNodeKey[i - 1] == 0) break;
	}

	for (int j = 0; j < i; j++) {
		insertion(treeNodeKey[j]);
	}
	
	postorder(root);

	return 0;
}

treePointer modifiedSearch(treePointer node, int k) {
	if (!node) return NULL;
	if (node->key > k) {
		if (!node->leftChild) return node;
		else if (node->leftChild < k) return node;
		else return modifiedSearch(node->leftChild, k);
	}
	else {
		if (!node->rightChild) return node;
		else if (node->rightChild < k) return node;
		else return modifiedSearch(node->rightChild, k);
	}
}

void insertion(int k) {
	if (k == 0) return;
	treePointer ptr, temp = modifiedSearch(root, k);

	if (temp || !root) {
		ptr = (treePointer)malloc(sizeof(Tree));
		ptr->key = k;
		ptr->rightChild = NULL;
		ptr->leftChild = NULL;
		if (root) {
			if (k < temp->key) temp->leftChild = ptr;
			else temp->rightChild = ptr;
		}
		else {
			root = ptr;
		}
	}
}

void postorder(treePointer cur) {
	if (cur) {
		postorder(cur->leftChild);
		postorder(cur->rightChild);
		printf("%d\n", cur->key);
	}
}