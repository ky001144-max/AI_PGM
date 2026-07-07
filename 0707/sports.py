from datetime import datetime
import asyncio
import edge_tts
import os
import tkinter as tk
from tkinter import messagebox
import threading

OUTPUT_FILE = "news_Son_edge.mp3"
VOICE = "ko-KR-SunHiNeural"  # 여성 아나운서 스타일

# --- 🔊 파이썬 3.14 표준 비동기 처리 함수 ---
async def main_tts_flow(news_text):
    """
    파이썬 3.14가 요구하는 정식 비동기 Task 형태로 
    음성 생성과 파일 저장을 하나의 흐름 안에서 처리합니다.
    """
    communicate = edge_tts.Communicate(news_text, VOICE)
    # create_task를 통해 정식 비동기 태스크로 등록하여 파이썬 3.14 검증 통과
    task = asyncio.create_task(communicate.save(OUTPUT_FILE))
    await task

def play_voice(news_text):
    """
    Tkinter 창이 멈추지 않도록 완전히 분리된 독립 쓰레드에서
    새로운 asyncio 루프를 처음부터 끝까지 깨끗하게 실행합니다.
    """
    def run():
        # 주피터 노트북 루프와 완전히 격리된 새 루프 생성
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        try:
            # 완벽히 격리된 환경에서 asyncio.run 효과를 내어 Timeout 에러 원천 차단
            new_loop.run_until_complete(main_tts_flow(news_text))
            
            # 음성 생성이 완벽히 성공한 후 플레이어 재생
            os.system(f"start /min wmplayer /play /close {OUTPUT_FILE}")
        except Exception as e:
            print(f"비동기 음성 재생 오류: {e}")
        finally:
            new_loop.close()

    threading.Thread(target=run, daemon=True).start()

# --- 📝 기사 작성 및 버튼 이벤트 함수 ---
def create_news():
    place = entry_place.get().strip()
    time_str = entry_time.get().strip()
    opponent = entry_opponent.get().strip()
    goals = entry_goals.get().strip()
    aids = entry_aids.get().strip()
    score_me = entry_score_me.get().strip()
    score_you = entry_score_you.get().strip()
    
    if not (place and time_str and opponent and goals and aids and score_me and score_you):
        messagebox.showwarning("입력 오류", "모든 칸을 빠짐없이 입력해주세요!")
        return

    try:
        g = int(goals)
        a = int(aids)
        my_score = int(score_me)
        your_score = int(score_you)
    except ValueError:
        messagebox.showerror("입력 오류", "골 수와 점수 칸에는 숫자만 입력할 수 있습니다!")
        return

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    news = f"[프리미어 리그 속보] ({current_time})\n"
    news += f"손흥민 선수는 {place}에서 {time_str}에 열린 경기에 출전하였습니다.\n"
    news += f"상대 팀은 {opponent}입니다. "

    if my_score > your_score:
        news += f"손흥민 선수의 팀이 {score_me}골을 넣어 {score_you}골을 넣은 상대 팀을 이겼습니다.\n"
    elif my_score < your_score:
        news += f"손흥민 선수의 팀이 {score_me}골을 넣어 {score_you}골을 넣은 상대 팀에게 졌습니다.\n"
    else:
        news += f"두 팀은 {score_me}대 {score_you}로 비겼습니다.\n"

    if g > 0 and a > 0:
        if my_score > your_score:
            news += f"손흥민 선수는 {goals}골에 도움 {aids}개로 승리를 크게 이끌었습니다.\n"
        elif my_score < your_score:
            news += f"손흥민 선수는 {goals}골에 도움 {aids}개로 대활약했으나, 팀의 패배로 빛이 바랬습니다.\n"
        else:
            news += f"손흥민 선수는 {goals}골에 도움 {aids}개를 기록하며 팀의 무승부에 기여했습니다.\n"
    elif g > 0 and a == 0:
        if my_score > your_score:
            news += f"손흥민 선수는 {goals}골로 승리를 이끌었습니다.\n"
        elif my_score < your_score:
            news += f"손흥민 선수는 {goals}골을 넣으며 분전했으나 팀의 패배를 막지 못했습니다.\n"
        else:
            news += f"손흥민 선수의 {goals}골 활약 속에 팀은 무승부를 거두었습니다.\n"
    elif g == 0 and a > 0:
        if my_score > your_score:
            news += f"손흥민 선수는 골은 없지만 도움 {aids}개로 승리하는 데 공헌하였습니다.\n"
        else:
            news += f"손흥민 선수는 도움 {aids}개를 기록하며 팀을 도왔으나 아쉽게 마무리되었습니다.\n"
    else:
        news += "아쉽게도 이번 경기에서 손흥민의 발끝은 침묵을 지켰습니다.\n"

    print("-" * 40)
    print(news)
    print("-" * 40)
    
    # 정석 비동기 쓰레드 재생 엔진 호출
    play_voice(news)
    
    # 윈도우 알림창으로 기사 보여주기
    messagebox.showinfo("생성된 기사", news)

# --- 🖼️ Tkinter GUI 창 구성하기 ---
root = tk.Tk()
root.title("스포츠 기사 자동 생성기")
root.geometry("380x340")
root.resizable(False, False)

title_label = tk.Label(root, text="⚽ 경기 정보를 입력하세요", font=("돋움", 11, "bold"), fg="#333333")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

labels = ["경기가 열린 곳은?", "경기가 열린 시간은?", "상대 팀은?", "손흥민의 골 수는?", "손흥민의 도움 수는?", "손흥민 팀 골 수?", "상대 팀 골 수?"]
entries = []

for i, text in enumerate(labels):
    lbl = tk.Label(root, text=text, width=18, anchor="e")
    lbl.grid(row=i+1, column=0, padx=10, pady=4)
    
    entry = tk.Entry(root, width=20)
    entry.grid(row=i+1, column=1, padx=10, pady=4)
    entries.append(entry)

entry_place, entry_time, entry_opponent, entry_goals, entry_aids, entry_score_me, entry_score_you = entries

btn_submit = tk.Button(root, text="📰 기사 생성 및 음성 듣기", command=create_news, bg="#4CAF50", fg="white", font=("돋움", 10, "bold"), cursor="hand2")
btn_submit.grid(row=len(labels)+1, column=0, columnspan=2, pady=15, ipadx=20, ipady=3)

root.mainloop()