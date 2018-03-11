/*
  g++ extraire_liste_mots.cpp
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
 
using namespace std;
 
int main(int argc, char **argv) {

  if(argc == 1 || argc>3) {
    cout << "./a.out /chemin/vers/frwiktionary-latest-pages-articles.xml" << endl;
    cout << "./a.out /chemin/vers/frwiktionary-latest-pages-articles.xml fr" << endl
	 << "pour recuperer la liste de tous les mots en français." << endl
	 << "Remplacer \"fr\" par \"en\" pour une liste de mots en anglais" << endl
	 << "Par defaut, la langue est le francais." << endl
	 << "Verifier que le code de langue est correct ; aucune verification n'est effectuee." << endl;
    return 0;
  }
  string nomFichier = argv[1];
  string codeLangue = "fr";
  if(argc==3)  codeLangue = argv[2];
  
  //https://dumps.wikimedia.org/frwiktionary/latest/frwiktionary-latest-pages-articles.xml.bz2
  ifstream infile(nomFichier.c_str(),ifstream::in);
  if(!infile) {
    cout << "Le fichier " << nomFichier << " n'existe pas" << endl;
    return 0;
  }

  string nomFichierSortie = "liste_" + codeLangue + ".txt";
  ofstream out(nomFichierSortie.c_str(),ofstream::out);
  if(!out) {
    cout << "Probleme avec le fichier de sortie" << endl;
    return 0;
  }
 
  string titre;
  string ns;
 
  string line;
  size_t pos1, pos2;
  unsigned int cmpt = 0;

  while(getline(infile,line)) {
    if(line.find("<page>")!=string::npos) {
      bool langue = false;
      while(getline(infile,line)) {
	if(line.find("<title>")!=string::npos) {
	  // on extrait le titre des balises <title>
	  pos1  = line.find("<title>");
	  pos2  = line.find("</title>");
	  titre = line.substr(pos1+7,pos2-pos1-7);
	} 

	if(line.find("<ns>")!=string::npos) {
	  //on vérifie que l'espace de nom est bien « 0 »
	  pos1 = line.find("<ns>");
	  pos2 = line.find("</ns>");
	  ns   = line.substr(pos1+4,pos2-pos1-4);
	}

	if(line.find("{{langue|" + codeLangue + "}}")!=string::npos) {
	  langue=true;
	}
	
	if(line.find("</page>")!=string::npos)
	  break;
      }
 
      if(ns=="0" && langue) {
	out  << titre << endl;
	cmpt++;
	if(cmpt%10000==0)
	  cout << cmpt << "\t" << titre << endl;
      } 
    }
    // if(cmpt==10) break;
  }
  infile.close();
  out.close();
 
  cout << cmpt << " articles trouves" << endl;
  return 1;
}
