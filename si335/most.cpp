#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <cmath>
#include <locale>
#include <algorithm>

using namespace std;

//FUNCTIONS
bool isSimilarSameLength(string,string,int);
bool isSimilarDeltaOne(string,string,int);

int main(int argc, char *argv[]){


  //VAR INIT
  fstream file;
  string filename, rawName;
  int countUpTo = 0;
  map<int,vector<string>> nameList_byLength;
  map<string,int> mispeleability;
  map<string,int> counts;
  map<string,int> sizes;
  map<string,vector<string>> pairings;
  locale loc;

  //IO
  //cout << "File: ";
  //cin >> filename;
  //cout << "Count: ";
  //cin >> countUpTo;
  filename = argv[1];
  int value = 0,length = 0;
  for(int i = 0;argv[2][i] != '\0'; i++){length += 1;}
  for(int i = 0; i < length; i++){value += pow(10,(length-i-1))*(argv[2][i]-48);}
  file.open(filename);
  countUpTo = value;

  // INITIAL READ and COUNT LOOP O(kn)
  while(file >> rawName){
    int length = rawName.length();
    string builtName = tolower(rawName[0],loc) + rawName.substr(1,length-1);
    //IF WEVE SEEN IT ALREADY
    if(counts.count(builtName)){
      counts[builtName] += 1;
    }
    //IF ITS A NEW NAME
    else{
      nameList_byLength[length].push_back(builtName);
      counts[builtName] = 1;
      sizes[builtName] = length;
      vector<string> temp;
      pairings[builtName] = temp;
    }
  }

  //FIND ALL PAIRINGS OF SIMILAR NAMES
  //SINCE THE PAIR ORDER IS NON_UNIQE, WE CAN SAVE THE REVERSE PAIR
  //AND FINALLY DELETE THE ROOT NAME
  for(auto item : counts){
    string root = item.first;
    int count = sizes[root];
    int deleteIndex = 0;


    //ONLY SEARCH NAMES THAT ARE WITHIN +- 1 LENGTH
    for(auto name : nameList_byLength[count-1]){
      if(isSimilarDeltaOne(root,name, count)){
        pairings[root].push_back(name);
        pairings[name].push_back(root);
      }
    }
    for(unsigned int i = 0; i < nameList_byLength[count].size(); i++){
      string name = nameList_byLength[count][i];
      if(isSimilarSameLength(root,name, count)){
        pairings[root].push_back(name);
        pairings[name].push_back(root);
        if(name == root){
          deleteIndex = i;
        }
      }
    }
    for(auto name : nameList_byLength[count+1]){
      if(isSimilarDeltaOne(name,root,count+1)){
        pairings[root].push_back(name);
        pairings[name].push_back(root);
      }
    }

    //COMPUTE THE MISPELEABILITY OF THIS NAME
    double sum = 0;
    int rootCount = counts[root];
    for(auto name : pairings[root]){
      if(counts[name] < rootCount){
        sum += counts[name];
      }
    }

    //SAVE IT
    mispeleability[root] = round(100*(sum/item.second));
    //DELETE THIS ROOT NAME SO WE DONT HAVE TO CHECK THORUGH IT AGAIN
    nameList_byLength[count].erase(nameList_byLength[count].begin()+deleteIndex);
  }

  //GET TOP 10 AND PRINT THEM
  vector<string> topTen;
  if(countUpTo > mispeleability.size()){
    cout << "ERROR: Count " << countUpTo << " exceeds size of list!" << endl;
    return -1;
  }
  for(int i = 0; i < countUpTo; i++){
    int max = 0;
    string max_item;
    for(auto item : mispeleability){
      if(item.second > max && !(find(topTen.begin(), topTen.end(),item.first) != topTen.end())){
        max = item.second;
        max_item = item.first;
      }
    }
    topTen.insert(topTen.end(),max_item);
  }
  for(string name : topTen){
    cout << toupper(name[0],loc) + name.substr(1,name.length()-1) << " " << mispeleability[name] << endl;
  }
}

//DETERMINE IF 2 EQUAL LENGTH STRINGS ARE SIMILAR
bool isSimilarSameLength(string name, string name2, int Len){
  int fails = 0;
  for(int i = 0; i < Len;i++){
    if(!(name[i] == name2[i])){
      fails += 1;
      if(fails > 1){
        return false;
      }
    }
  }
  return true;
}
//DETERMINES IF 2 NAMES OF LENGTH +- 1 ARE SIMLIAR
//ESSENTIALLY, RUN THROUGH THE LONGER NAME AND MAKE SURE ONLY ONE LETTER IS OFF
bool isSimilarDeltaOne(string nameHigh, string nameLow, int nameHighLen){
  int first_break = 0;
  for(int i = 0; i < nameHighLen;i++){
    char letter = nameHigh[i];
    if(!(letter == nameLow[i])){
      first_break = i;
      break;
    }
  }
  first_break += 1;
  for(int i = first_break; i < nameHighLen; i++){
    char letter = nameHigh[i];
    if(!(letter == nameLow[i-1])){
      return false;
    }
  }
  return true;
}
