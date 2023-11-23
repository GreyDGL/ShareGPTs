# ShareGPTs: Retrieval and Sharing of GPTs Instructions


<div align="center">
<img src=logo.png width=500 height=300 >
</div>

## Introduction
🎯 Unleash the power of GPTs with ease! Our project automates the collection and sharing of prompts, sparking a world of creativity and inspiration.

In this project, we implement an automatic tool that helps to retrieve the instructions in GPTs using the strategy of [prompt injection](https://arxiv.org/abs/2306.05499).

## Disclaimer
This tool is developed for educational purpose only, and distributed under MIT license. The authors are not responsible for any potential damages caused by the tool, nor condemn any potential illegal use of the tool.
Upon the usage of the tool, you agree that you are responsible for your own actions. Your usage log (retrieved GPTs and prompts) will be collected for research purpose.

## How to use the tool
1. Prepare the URL of the target GPTs. You may refer to the following lists.
   * [Awesome-GPTs](https://github.com/ai-boost/Awesome-GPTs) [Curated list of awesome GPTs]
   * [BestGPTs](https://github.com/AgentOps-AI/BestGPTs) [Top ranked OpenAI GPTs]
   * [awesome-gpts](https://github.com/taranjeet/awesome-gpts) [Collection of all the GPTs created by the community]
   * [linexjlin/GPTs](https://github.com/linexjlin/GPTs) [leaked prompts of GPTs]
   * [friuns2/Awesome-GPTs-Big-List](https://github.com/friuns2/Awesome-GPTs-Big-List) [Use OpenAI GPTs for Free, [GPTs Store](https://gptcall.net/)]
   * [all-in-aigc/gpts-works](https://github.com/all-in-aigc/gpts-works) [A Third-party GPTs store [GPTs Works](https://gpts.works/)]
   * [lxfater/Awesome-GPTs](https://github.com/lxfater/Awesome-GPTs) [1000+ GPTs and 10 categories. 80+ Leaked Prompt，Awesome，chatgpt，Ai，prompt]
   * [EmbraceAGI/Awesome-AI-GPTs](https://github.com/EmbraceAGI/Awesome-AI-GPTs) [Awesome AI GPTs, OpenAI GPTs, GPT-4, ChatGPT, GPTs, Prompts, plugins, Prompts leaking]
   * [Anil-matcha/Awesome-GPT-Store](https://github.com/Anil-matcha/Awesome-GPT-Store) [Awesome AI GPTs, OpenAI GPTs, GPT-4, ChatGPT, GPTs, Prompts, plugins, Prompts leaking]
   * [imartinez/privateGPT](https://github.com/imartinez/privateGPT) [About Interact with your documents using the power of GPT, 100% privately, no data leaks]
   * [fr0gger/Awesome-GPT-Agents](https://github.com/fr0gger/Awesome-GPT-Agents) [A curated list of GPT agents for cybersecurity]
   * [Link-AGI/AutoAgents](https://github.com/Link-AGI/AutoAgents)  [Generate different roles for GPTs to form a collaborative entity for complex tasks]
   * [promptslab/Awesome-Openai-GPTs](https://github.com/promptslab/Awesome-Openai-GPTs) [About Awesome GPTs]
   * [GPTs Hunter](https://www.gptshunter.com/) [Discover GPT Store]
2. The tool relies on the [GPT4OpenAI](https://github.com/Erol444/gpt4-openai-api). You shall obtain the session token from the ChatGPT website following [how to get the session token](#how-to-get-the-session-token) section below. You can put it into `SESSION_TOKEN` file.
3. Install the tool
   - Create a virtual environment if needed: `virtualenv venv`, `source venv/bin/activate`
   - Install the dependencies: `pip3 install -r requirements.txt`
4. Run based on the following automatic code.
```commandline
python3 main.py --url <url> --cookie <session_token> -- output <output_file>
```
  Example: you may use `python3 main.py --url https://chat.openai.com/g/g-PDWi5Scbc-all-around-teacher-learn-everything-in-3-min`

5. Examine the output in output file, by default `GPTs_sysprompts.csv`. Note that there's a rate limit of 60s after each attempt, so the tool will execute for at least 60s before saving the results.


## How to get the session token

1. Go to https://chat.openai.com and open the developer tools by `F12`.
2. Find the `__Secure-next-auth.session-token` cookie in `Application` > `Storage` > `Cookies` > `https://chat.openai.com`.
3. Copy the value in the `Cookie Value` field.
4. The obtained token shall either be stored in file `SESSION_TOKEN` or passed to the tool through the arg parser.

![image](https://user-images.githubusercontent.com/19218518/206170122-61fbe94f-4b0c-4782-a344-e26ac0d4e2a7.png)

## Contact the Contributors!
* [Gelei Deng] - gelei.deng@ntu.edu.sg
* [Weitao Feng] - weitaofeng@mail.ustc.edu.cn
* [Jie Zhang] - jie_zhang@ntu.edu.sg
* [Jiyan He] - hejiyan@mail.ustc.edu.cn
