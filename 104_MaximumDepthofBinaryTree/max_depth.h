#ifndef MAX_DEPTH
#define MAX_DEPTH

#include <stdio.h>

//https://github.com/junjizhi/fifo
#define QueueElement struct TreeNode *
#include "fifo/queue.h"

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int maxDepth(struct TreeNode* root);
struct TreeNode *deserializer(int tree_arr[], int len);
void visualize(struct TreeNode *root, int len);

#endif
