#ifndef SimG4CMS_HCalSD_h
#define SimG4CMS_HCalSD_h
///////////////////////////////////////////////////////////////////////////////
// File: HCalSD.h
// Description: Stores hits of Hadron calorimeter in appropriate container
// Use in your sensitive detector builder:
//    HCalSD* hcalSD = new HCalSD(SDname, new CaloNumberingScheme());
///////////////////////////////////////////////////////////////////////////////

#include "SimG4CMS/Calo/interface/CaloSD.h"
#include "SimG4CMS/Calo/interface/HFShower.h"
#include "SimG4CMS/Calo/interface/HFShowerLibrary.h"
#include "SimG4CMS/Calo/interface/HFShowerParam.h"
#include "SimG4CMS/Calo/interface/HFShowerPMT.h"
#include "SimG4CMS/Calo/interface/HFShowerFibreBundle.h"
#include "SimG4CMS/Calo/interface/HcalNumberingScheme.h"
#include "DetectorDescription/Core/interface/DDsvalues.h"
#include "Geometry/HcalCommonData/interface/HcalNumberingFromDDD.h"

#include "G4String.hh"
#include <map>
#include <string>
#include <TH1F.h>

class DDCompactView;
class DDFilteredView;
class G4LogicalVolume;
class G4Material;
class G4Step;

class HCalSD : public CaloSD {

public:    

  HCalSD(G4String , const DDCompactView &, SensitiveDetectorCatalog &,
         edm::ParameterSet const &, const SimTrackManager*);
  virtual ~HCalSD();
  virtual bool                  ProcessHits(G4Step * , G4TouchableHistory * );
  virtual double                getEnergyDeposit(G4Step* );
  virtual uint32_t              setDetUnitId(G4Step* step);
  void                          setNumberingScheme(HcalNumberingScheme* );

protected:

  virtual void                  initRun();
  virtual bool                  filterHit(CaloG4Hit*, double);

private:    

  uint32_t                      setDetUnitId(int, G4ThreeVector, int, int);
  std::vector<double>           getDDDArray(const std::string&, 
                                            const DDsvalues_type&);
  std::vector<G4String>         getNames(DDFilteredView&);
  bool                          isItHF(G4Step *);
  bool                          isItHF(G4String);
  bool                          isItFibre(G4LogicalVolume*);
  bool                          isItFibre(G4String);
  bool                          isItPMT(G4LogicalVolume*);
  bool                          isItStraightBundle(G4LogicalVolume*);
  bool                          isItConicalBundle(G4LogicalVolume*);
  bool                          isItScintillator(G4Material*);
  void                          getFromLibrary(G4Step * step);
  void                          hitForFibre(G4Step * step);
  void                          getFromParam(G4Step * step);
  void                          getHitPMT(G4Step * step);
  void                          getHitFibreBundle(G4Step * step, bool type);
  int                           setTrackID(G4Step * step);
  void                          readWeightFromFile(std::string);
  double                        layerWeight(int, G4ThreeVector, int, int);
  void                          plotProfile(G4Step* step, G4ThreeVector pos, 
                                            double edep, double time, int id);

  HcalNumberingFromDDD*         numberingFromDDD;
  HcalNumberingScheme*          numberingScheme;
  HFShowerLibrary *             showerLibrary;
  HFShower *                    hfshower;
  HFShowerParam *               showerParam;
  HFShowerPMT *                 showerPMT;
  HFShowerFibreBundle *         showerBundle;
  bool                          useBirk, useLayerWt, useFibreBundle, applyFidCut;
  double                        birk1, birk2, birk3, betaThr;
  bool                          useHF, useShowerLibrary, useParam, usePMTHit;
  double                        eminHitHB, eminHitHE, eminHitHO, eminHitHF;
  G4int                         mumPDG, mupPDG; 
  std::vector<double>           layer0wt;
  std::vector<G4LogicalVolume*> hfLV;
  std::vector<G4String>         hfNames;
  std::vector<int>              hfLevels;
  std::vector<G4LogicalVolume*> fibreLV;
  std::vector<G4String>         fibreNames;
  std::vector<G4String>         matNames;
  std::vector<G4Material*>      materials;
  std::vector<G4LogicalVolume*> pmtLV, fibre1LV, fibre2LV;
  std::map<uint32_t,double>     layerWeights;
  TH1F                          *hit_[9], *time_[9], *dist_[9];

};

#endif // HCalSD_h
