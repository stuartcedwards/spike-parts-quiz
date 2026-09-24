from PIL import Image
import os
os.makedirs("assets",exist_ok=True)
groups=[
(range(1,6),"IMG_06387A50-B0E8-4362-8C70-959E4647EDCC.jpeg",.02,.98,.485,.625),
(range(6,11),"IMG_0685AE32-88F3-45F4-902B-5F5D41763A83.jpeg",.04,.98,.455,.615),
(range(11,16),"IMG_0E92943C-45E2-4AB6-B210-4CC090A9B561.jpeg",.03,.98,.475,.615),
(range(16,21),"IMG_2C136707-C845-4869-98C2-18C0819DAAD7.jpeg",.02,.98,.485,.615),
(range(21,25),"IMG_401BA366-0249-422E-8DAE-FF0BF2F2B7DF.jpeg",.02,.98,.475,.625),
(range(25,27),"IMG_43E29AC4-8568-4375-9E32-F5BAEE735B6F.jpeg",.20,.88,.475,.685),
(range(27,30),"IMG_46DC24D6-47FC-40EA-AD30-AA2D0F6684E3.jpeg",.05,.98,.475,.625),
(range(30,33),"IMG_60B81712-E580-473B-9DD6-E4949BB1E35E.jpeg",.03,.98,.485,.635),
(range(33,38),"IMG_651A4E2F-E18A-4123-97D4-09F15FCF6F69.jpeg",.02,.98,.455,.625),
(range(38,39),"IMG_67CBB269-B9D9-49DE-8E31-ED0DED759A01.jpeg",.32,.78,.435,.665),
(range(39,43),"IMG_6FE718BD-85CF-43F6-B2B5-87665FC63152.jpeg",.02,.98,.455,.635),
(range(43,47),"IMG_824A9A4F-04BA-4DA7-B6BD-602CAA68D8D8.jpeg",.02,.98,.475,.615),
(range(47,50),"IMG_82FC1712-359C-472D-B51D-3E772E312E5E.jpeg",.02,.98,.475,.625),
(range(50,55),"IMG_9F9DB632-A67D-41E8-A3D0-E70D2F0BD8AD.jpeg",.04,.98,.465,.615),
(range(55,60),"IMG_A0E68553-2F4C-427B-8AA5-228561A9BBB7.jpeg",.02,.98,.485,.625),
(range(60,63),"IMG_ABECFE0C-E0C6-47DD-A8E1-D83EE94D58E0.jpeg",.05,.98,.455,.635),
(range(63,67),"IMG_B32BF3C3-09CE-48F1-9D20-909B5FE3B43D.jpeg",.02,.98,.475,.625),
(range(67,72),"IMG_D08EA238-91E2-4C35-B09B-850A9D2BEFB1.jpeg",.02,.98,.475,.625),
(range(72,77),"IMG_D639049E-F9F3-4FD5-9967-8553A9F67ACF.jpeg",.02,.98,.475,.615),
(range(77,81),"IMG_DEA3278D-DE97-4F87-AC79-C38F9EA64577.jpeg",.05,.98,.475,.615),
(range(81,85),"IMG_DFDE91E5-F0F2-470C-BD15-00482973F957.jpeg",.02,.98,.475,.625),
(range(85,89),"IMG_E5533126-DC89-4BF8-B7EB-7A9DFDF8B23C.jpeg",.02,.98,.485,.615)]
for rng,fn,x0,x1,y0,y1 in groups:
 ids=list(rng); n=len(ids); im=Image.open(fn).convert("RGB"); W,H=im.size; cell=(x1-x0)/n
 for j,idx in enumerate(ids):
  a=x0+j*cell+cell*.06; b=x0+(j+1)*cell-cell*.06
  crop=im.crop((int(a*W),int(y0*H),int(b*W),int(y1*H)))
  canvas=Image.new("RGB",(600,400),"white"); crop.thumbnail((570,370))
  canvas.paste(crop,((600-crop.width)//2,(400-crop.height)//2))
  canvas.save(f"assets/part-{idx:02d}.jpg",quality=90)
