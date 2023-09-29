import time
import pygame

# ===================== 기본 설정 =====================

pygame.init()
pygame.mixer.init()
pygame.font.init()

# screen = pygame.display.set_mode(vars.SCREEN_RESOULUTION)
# pygame.display.set_caption(f"업무 떠넘기기 v{vars.VERSION}")


fpsClock = pygame.time.Clock()
run = True


# ===================== 화면 새로고침 =====================

lasttime = time.time()
while run:
	try:
		# print(f"{int(1/(time.time() - lasttime))} fps   ", end='\r')
		pass
	except:
		pass
	lasttime = time.time()

	# ========================= 변수 설정 =========================

	events = pygame.event.get()
	
	# ========================= 게임 시스템 =========================

	# PageManager.update(screen, events,
	# 	    **{
	# 			'font' : font,
	# 			'PageManager' : PageManager,
	# 			'ScriptManager' : ScriptManager,
	# 			'DB' : DB,
	# 		}
	# 	)

	# ========================= 그리기 =========================

	

	# ========================= 클릭 이벤트 처리 =========================
	for event in events:
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
	
	pygame.display.update()

	fpsClock.tick(vars.FPS)
	