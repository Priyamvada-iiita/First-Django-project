/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include<iostream>
using namespace std;
#include<bits/stdc++.h>

int main(){
    string a;
    string b; 
    cin>>a>>b;
    int ans =0;
map<int, vector<int>> m;
for(int i =1; i<=a.size(); i++){
    m[a[i]-'a'].push_back(i);
}
int pre = 0, curr=0;
for(auto c:b){
    auto itr = m.find(c-'a');
    auto k = itr->second;
    auto itr2 = upper_bound(k.begin(), k.end(), pre);
    curr = k[itr2-k.begin()];
    if( itr2 == k.end()) curr= k[0]; 
    if( pre<curr){ 

    ans += curr- pre ;
    }
    else{
        ans += a.size() - pre + curr ;
    }
  pre = curr;

}
cout<<ans;
}