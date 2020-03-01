#include <stdio.h>
#include <algorithm>
#include<climits>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return curisValidBST(root,LONG_LONG_MIN,LONG_LONG_MAX);
    }
    bool curisValidBST(TreeNode* root,long long minval,long long maxval) {
        if (root==NULL){
           return true;
        };
        if(root->val>=maxval||root->val<=minval){
           return false;
        };
        return curisValidBST(root->left,minval,root->val)&&curisValidBST(root->right,root->val,maxval);
    }
};
int main(){
   struct TreeNode roov(2147483647);
   TreeNode* root=&roov;
   Solution n;
   printf("%d",n.isValidBST(root));
}