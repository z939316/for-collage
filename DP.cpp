#include <iostream>
#include <cstring>
using namespace std;
string cname[101];
int v[101],w[101],k[1001],p[101][1001];
int ks,n;
int main(){
    cout << "�`�@���h�֭�����ܡH" << endl;
    cin >> n;
    cout <<"�п�J'�����W��' '���q' ������'�A�O�o�H�Ů�j�}��"<<endl;
    for(int i=0;i<n;i++){
      cin>>cname[i]>>v[i]>>w[i];
    }
    cout << "�A�������׷�������H" << endl;
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
    cout << "�A�̦h������`���q�G"<<endl << k[ks] << endl;
    int j=ks;
    cout << "�A�ӦY���G"<< endl;
    for (int i=n-1;i>=0;i--){
      if(p[i][j]>=0){
        cout << cname[i] << ' ';
        j=j-w[i];
      }
    }
}
