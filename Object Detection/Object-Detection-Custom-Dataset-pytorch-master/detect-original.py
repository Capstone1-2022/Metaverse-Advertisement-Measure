from torchvision import transforms
from utils import *
from PIL import Image, ImageDraw, ImageFont
import warnings
warnings.filterwarnings("ignore")


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model checkpoint
# Transforms
resize = transforms.Resize((300, 300))
to_tensor = transforms.ToTensor()
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])


def detect(original_image, min_score, max_overlap, top_k, suppress=None , model=None):
    """
    Detect objects in an image with a trained SSD300, and visualize the results.

    :param original_image: image, a PIL Image
    :param min_score: minimum threshold for a detected box to be considered a match for a certain class
    :param max_overlap: maximum overlap two boxes can have so that the one with the lower score is not suppressed via Non-Maximum Suppression (NMS)
    :param top_k: if there are a lot of resulting detection across all classes, keep only the top 'k'
    :param suppress: classes that you know for sure cannot be in the image or you do not want in the image, a list
    :return: annotated image, a PIL Image
    """

    # Transform
    image = normalize(to_tensor(resize(original_image)))

    # Move to default device
    image = image.to(device)

    # Forward prop.
    predicted_locs, predicted_scores = model(image.unsqueeze(0))

    # Detect objects in SSD output
    det_boxes, det_labels, det_scores = model.detect_objects(predicted_locs, predicted_scores, min_score=min_score,
                                                             max_overlap=max_overlap, top_k=top_k)

    # Move detections to the CPU
    det_boxes = det_boxes[0].to('cpu')

    # Transform to original image dimensions
    original_dims = torch.FloatTensor(
        [original_image.width, original_image.height, original_image.width, original_image.height]).unsqueeze(0)
    det_boxes = det_boxes * original_dims

    # Decode class integer labels
    det_labels = [rev_label_map[l] for l in det_labels[0].to('cpu').tolist()]

    # If no objects found, the detected labels will be set to ['0.'], i.e. ['background'] in SSD300.detect_objects() in model.py
    if det_labels == ['background']:
        # Just return original image
        return original_image

    # Annotate
    annotated_image = original_image
    draw = ImageDraw.Draw(annotated_image)
    font = ImageFont.truetype("./arial.ttf", 15)

    # Suppress specific classes, if needed
    for i in range(det_boxes.size(0)):
        if suppress is not None:
            if det_labels[i] in suppress:
                continue

        # Boxes
        box_location = det_boxes[i].tolist()
        draw.rectangle(xy=box_location, outline=label_color_map[det_labels[i]])
        draw.rectangle(xy=[l + 1. for l in box_location], outline=label_color_map[
            det_labels[i]])  # a second rectangle at an offset of 1 pixel to increase line thickness
        # draw.rectangle(xy=[l + 2. for l in box_location], outline=label_color_map[
        #     det_labels[i]])  # a third rectangle at an offset of 1 pixel to increase line thickness
        # draw.rectangle(xy=[l + 3. for l in box_location], outline=label_color_map[
        #     det_labels[i]])  # a fourth rectangle at an offset of 1 pixel to increase line thickness

        # Text
        text_size = font.getsize(det_labels[i].upper())
        text_location = [box_location[0] + 2., box_location[1] - text_size[1]]
        textbox_location = [box_location[0], box_location[1] - text_size[1], box_location[0] + text_size[0] + 4.,
                            box_location[1]]
        draw.rectangle(xy=textbox_location, fill=label_color_map[det_labels[i]])
        draw.text(xy=text_location, text=det_labels[i].upper(), fill='white',
                  font=font)
    del draw

    return annotated_image

test=[
'frame0004_jpg.rf.836163e1d1bce92c1d4c59b846084f23',
'frame0018_jpg.rf.333e97e1cebadcb93c2fa0fa1500d032',
'frame0029_jpg.rf.5ad1301e025382a2a599dd70b384ec82',
'frame0034_jpg.rf.b2b395b3f74768f465896f5acd7d439e',
'frame0057_jpg.rf.678f3e601011228492a64c44c594ebc8',
'frame0076_jpg.rf.5b97fba7d1b3582b5aaafb81fa31c73e',
'frame0132_jpg.rf.61f61aa3e2902869e420ef9b72745189',
'frame0143_jpg.rf.a463580ce100645a2feecfd6967f57fc',
'frame0145_jpg.rf.5202b01af0726465c77f3922dc8c5b40',
'frame0238_jpg.rf.73a119308379a6029e5cf290230120f1',
'frame0287_jpg.rf.2259ff1c26031219c52b7ee015e438cc',
'frame0360_jpg.rf.484b908ecb88686d0cc9c54673f5ce9a',
'frame0565_jpg.rf.17b507ebfaa62e2340983ac00061dfde',
'frame0695_jpg.rf.0142a1f1e3a6d7438446b0dc84e5491e'
]

if __name__ == '__main__':
	# checkpoint = 'BEST_pretrained_optimizercheckpoint_ssd300.pth.tar'
	# checkpoint = 'BEST_pretrained_optimizercheckpoint_ssd300.pth.tar'
	# checkpoint = 'BEST_sgd_scratchcheckpoint_ssd300.pth.tar'
	checkpoint = 'BEST_checkpoint_ssd300.pth.tar'
	
	
	# checkpoint = 'BEST_checkpoint_ssd300.pth.tar'
	checkpoint = torch.load(checkpoint, map_location=device)
	start_epoch = checkpoint['epoch'] + 1
	best_loss = checkpoint['loss']
	print('\nLoaded checkpoint from epoch %d. Best loss so far is %.3f.\n' % (start_epoch, best_loss))
	model = checkpoint['model']
	model = model.to(device)
	model.eval()
	num=0
	for i in test:
		img_path = '../datasets/roblox/roblox data/JPEGImages/'+i+'.jpg'
		original_image = Image.open(img_path, mode='r')
		original_image = original_image.convert('RGB')
		try:
			os.mkdir("verify/")
		except OSError:
			None
		detect_path="verify/detection-"+str(num)+".jpg"
		num+=1
		detect(original_image, min_score=0.2, max_overlap=0.1, top_k=1000, model=model).save(detect_path, "JPEG")
