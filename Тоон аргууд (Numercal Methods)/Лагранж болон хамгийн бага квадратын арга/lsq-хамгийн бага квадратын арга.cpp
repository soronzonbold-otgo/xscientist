/* Шугаман тэгшитгэлийн параметрийг олох хамгийн бага квадратын аргад зориулан
c++ кодыг нэгмж өглөө.
*/


#include <fstream>
#include <stdio.h>
#include <vector>
#include <cassert>
#include <iostream>
#include <math.h> 
#include<algorithm>

using namespace std;

double inverting_2x2_matrix(vector<double> &mat,double a, double b){

vector<double> multiplication(4);

double det,invdet;


det=mat[0]*mat[3]-mat[2]*mat[1];
invdet=1./det;

multiplication[0]=mat[3]*invdet;
multiplication[1]=-mat[1]*invdet;
multiplication[2]=-mat[2]*invdet;
multiplication[3]=mat[0]*invdet;


double C=multiplication[0]*a+multiplication[1]*b;
double D=multiplication[2]*a+multiplication[3]*b;

cout<<C<<' '<<D<<endl;


}


int main(){


	vector<double> x(10);
	vector<double> y(10);
	vector<double> t(4);

	ofstream myfile;
  	myfile.open ("example_2.txt");
  	  	

  	int s=0;
  	int sum=0;
	for(int i=0; i<10;i++){
		x[i]=i;
		y[i]=0.5*x[i]-1;
		s=s+pow(i,2);
		sum=sum+i;
		myfile << x[i]<<" "<<y[i]<<'\n';
	}
	myfile.close();

	int sy=0;
  	int sumy=0;
	for(int i=0; i<10;i++){
		sumy=sumy+y[i];
		sy=sy+x[i]*y[i];
	}

	t[0]=x.size();
	t[1]=sum;
	t[2]=sum;
	t[3]=s;

	inverting_2x2_matrix(t,sumy,sy);

	/* !!!!!!!!!!!!!!!!Be careful passing as return gives wrong value!!!!!!*/
	
	//double f,g;
	//f,g=det_2x2_matrix(t,sumy,sy);
	

	//cout<<f<<' '<<g<<endl;
	//cout<<sumy<<' '<<sy<<endl;

  	return 0;

}





