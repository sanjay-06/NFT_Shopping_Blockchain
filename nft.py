from PIL import Image
import random
import os

class NFT:
    
    def create_new_image(self,all_images):
            
            new_image = {} #

            # For each trait category, select a random trait based on the weightings 
            new_image ["Face"] = random.choices(self.face, self.face_weights)[0]
            new_image ["Ears"] = random.choices(self.ears, self.ears_weights)[0]
            new_image ["Eyes"] = random.choices(self.eyes, self.eyes_weights)[0]
            new_image ["Hair"] = random.choices(self.hair, self.hair_weights)[0]
            new_image ["Mouth"] = random.choices(self.mouth, self.mouth_weights)[0]
            new_image ["Nose"] = random.choices(self.nose, self.nose_weights)[0]
            
            if new_image in all_images:
                return self.create_new_image(all_images)
            else:
                return new_image
    
    def all_images_unique(self,all_images):
            seen = list()
            return not any(i in seen or seen.append(i) for i in all_images)
            
    def __init__(self) -> None:
        
        self.face = ["White", "Black"]
        self.face_weights = [60, 40]

        self.ears = ["No Earring", "Left Earring", "Right Earring", "Two Earrings"]
        self.ears_weights = [25, 30, 44, 1]

        self.eyes = ["Regular", "Small", "Rayban", "Hipster", "Focused"]
        self.eyes_weights = [70, 10, 5 , 1 , 14]

        self.hair = ['Up Hair', 'Down Hair', 'Mohawk', 'Red Mohawk', 'Orange Hair', 'Bubble Hair', 'Emo Hair',
        'Thin Hair',
        'Bald',
        'Blonde Hair',
        'Caret Hair',
        'Pony Tails']
        self.hair_weights = [10 , 10 , 10 , 10 ,10, 10, 10 ,10 ,10, 7 , 1 , 2]

        self.mouth = ['Black Lipstick', 'Red Lipstick', 'Big Smile', 'Smile', 'Teeth Smile', 'Purple Lipstick']
        self.mouth_weights = [10, 10,50, 10,15, 5]

        self.nose = ['Nose', 'Nose Ring']
        self.nose_weights = [90, 10]

        #Classify traits

        self.face_files = {
            "White": "face1",
            "Black": "face2"
        }

        self.ears_files = {
            "No Earring": "ears1",
            "Left Earring": "ears2",
            "Right Earring": "ears3",
            "Two Earrings": "ears4"
        }

        self.eyes_files = {
            "Regular": "eyes1",
            "Small": "eyes2",
            "Rayban": "eyes3",
            "Hipster": "eyes4",
            "Focused": "eyes5"     
        }

        self.hair_files = {
            "Up Hair": "hair1",
            "Down Hair": "hair2",
            "Mohawk": "hair3",
            "Red Mohawk": "hair4",
            "Orange Hair": "hair5",
            "Bubble Hair": "hair6",
            "Emo Hair": "hair7",
            "Thin Hair": "hair8",
            "Bald": "hair9",
            "Blonde Hair": "hair10",
            "Caret Hair": "hair11",
            "Pony Tails": "hair12"
        }


        self.mouth_files = {
            "Black Lipstick": "m1",
            "Red Lipstick": "m2",
            "Big Smile": "m3",
            "Smile": "m4",
            "Teeth Smile": "m5",
            "Purple Lipstick": "m6"
        }

        self.nose_files = {
            "Nose": "n1",
            "Nose Ring": "n2"   
        }
        
    def run_nft(self):
        

        ## Generate Traits

        TOTAL_IMAGES = 100 # Number of random unique images we want to generate

        all_images = [] 

        # A recursive function to generate unique image combinations
       
            
        # Generate the unique combinations based on trait weightings
        for i in range(TOTAL_IMAGES): 
            
            new_trait_image = self.create_new_image(all_images)
            
            all_images.append(new_trait_image)

        # Returns true if all images are unique
        

        print("Are all images unique?", self.all_images_unique(all_images))
        # Add token Id to each image
        i = 0
        for item in all_images:
            item["tokenId"] = i
            i = i + 1
        
        print(all_images)

        # Get Trait Counts

        face_count = {}
        for item in self.face:
            face_count[item] = 0
            
        ears_count = {}
        for item in self.ears:
            ears_count[item] = 0

        eyes_count = {}
        for item in self.eyes:
            eyes_count[item] = 0
            
        hair_count = {}
        for item in self.hair:
            hair_count[item] = 0
            
        mouth_count = {}
        for item in self.mouth:
            mouth_count[item] = 0
            
        nose_count = {}
        for item in self.nose:
            nose_count[item] = 0

        for image in all_images:
            face_count[image["Face"]] += 1
            ears_count[image["Ears"]] += 1
            eyes_count[image["Eyes"]] += 1
            hair_count[image["Hair"]] += 1
            mouth_count[image["Mouth"]] += 1
            nose_count[image["Nose"]] += 1
            
        print(face_count)
        print(ears_count)
        print(eyes_count)
        print(hair_count)
        print(mouth_count)
        print(nose_count)

        #### Generate Images
        os.mkdir(f'')

        for item in all_images:

            im1 = Image.open(f'./scripts/face_parts/face/{self.face_files[item["Face"]]}.png').convert('RGBA')
            im2 = Image.open(f'./scripts/face_parts/eyes/{self.eyes_files[item["Eyes"]]}.png').convert('RGBA')
            im3 = Image.open(f'./scripts/face_parts/ears/{self.ears_files[item["Ears"]]}.png').convert('RGBA')
            im4 = Image.open(f'./scripts/face_parts/hair/{self.hair_files[item["Hair"]]}.png').convert('RGBA')
            im5 = Image.open(f'./scripts/face_parts/mouth/{self.mouth_files[item["Mouth"]]}.png').convert('RGBA')
            im6 = Image.open(f'./scripts/face_parts/nose/{self.nose_files[item["Nose"]]}.png').convert('RGBA')

            #Create each composite
            com1 = Image.alpha_composite(im1, im2)
            com2 = Image.alpha_composite(com1, im3)
            com3 = Image.alpha_composite(com2, im4)
            com4 = Image.alpha_composite(com3, im5)
            com5 = Image.alpha_composite(com4, im6)

                            

        #Convert to RGB
        rgb_im = com5.convert('RGB')
        file_name = str(item["tokenId"]) + ".png"
        rgb_im.save("./html/images/" + file_name)

    def get_images(self):
        print("some")