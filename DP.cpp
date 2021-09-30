#include <iostream>
#include <cstring>
using namespace std;
string cname[101];
int v[101],w[101],k[1001],p[101][1001];
int ks,n;
int main(){
    cout << "總共有多少食物選擇？" << endl;
    cin >> n;
    cout <<"請輸入'食物名稱' '熱量' 飽食度'，記得以空格隔開喔"<<endl;
    for(int i=0;i<n;i++){
      cin>>cname[i]>>v[i]>>w[i];
    }
    cout << "你的飽食度極限為何？" << endl;
    cin>>ks;
    memset(k,0, sizeof(k));
    memset(p,-1, sizeof(p));
    for(int i=0;i<n;i++){
      for(int j=ks;j>=w[i];j--){
        if (k[j-w[i]]+v[i]>k[j]){
          k[j]=k[j-w[i]]+v[i];
          p[i][j]=i;
        }
      }
    }
    cout << "你最多攝取的總熱量："<<endl << k[ks] << endl;
    int j=ks;
    cout << "你該吃的："<< endl;
    for (int i=n-1;i>=0;i--){
      if(p[i][j]>=0){
        cout << cname[i] << ' ';
        j=j-w[i];
      }
    }
}
