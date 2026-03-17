# Coppelia Sim Setup Notes
Got Codex to run the following
- Installed podman on the host (Arch Linux) and configured its storage to live on the SSD drive.
- Pulled an ubuntu 22.04 based ros2 humble desktop container image.
- Made Ubuntu 22.04 CoppeliaSim binaries available inside that container.
- CoppeliaSim contains ROS2 plugin, so that ROS2 can interface with it.

Had issues with Qt for wayland, but Codex fixed this for me, by switching to X11. Now CoppeliaSim works.
Command to start CoppeliaSim:
```
FORCE_X11=1 /home/dominic/Projects/coppeliasim/run_coppeliasim_ros2_container.sh
```
These gets ROS started:
```
FORCE_X11=1 /home/dominic/Projects/coppeliasim/ros2_shell_container.sh
```

Make sure, when opening a script, you click right on the script icon.


**Executive Summary (Today’s Progress)**

- Set up CoppeliaSim to run via **X11** inside the ROS2 Humble container on the SSD.
- Downloaded and extracted CoppeliaSim to /home/dominic/Projects/coppeliasim/.
- Mounted dvrk_urdf into the container at /opt/dvrk_urdf.
- Generated URDFs from xacro:
    - [psm.classic.abs.urdf](https://file+.vscode-resource.vscode-cdn.net/home/dominic/.vscode-oss/extensions/openai.chatgpt-0.4.71-universal/webview/# "psm.classic.abs.urdf")
    - [patient_cart.classic.abs.urdf](https://file+.vscode-resource.vscode-cdn.net/home/dominic/.vscode-oss/extensions/openai.chatgpt-0.4.71-universal/webview/# "patient_cart.classic.abs.urdf")
- Imported the **full patient cart** into CoppeliaSim using the absolute‑path URDF (meshes loaded correctly).
- Fixed ROS2 plugin load by removing old sim.loadModule usage and loading via require('simROS2').
- Added a ROS2 bridge script and successfully **generated per‑joint ROS2 topics** (per‑joint /command and /state topics).
- Confirmed the correct topic list printed in the CoppeliaSim console (topics named like /dvrk/joint/_world_visual_.../command).

**Open Issues**

- ros2 topic list in the ROS2 shell was empty → likely **ROS2 domain/network mismatch** or ROS2 shell not in the container.
- Need to verify ROS2 shell is in the container and set ROS_DOMAIN_ID consistently.
- Joint motion still unverified from ROS2 commands.