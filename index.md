<h1 id="overview">Overview</h1>
 UAVA,<i>UAV-Assistant</i>,dataset is specifically designed for fostering applications which consider UAVs and humans as cooperative agents. We employ a real-world 3D scanned dataset (<a href="https://niessner.github.io/Matterport/">Matterport3D</a>
), physically-based shading, a gamiﬁed simulator for realistic drone navigation trajectory collection and randomized sampling, to generate multimodal data both from the user’s exocentric view of the drone, as well as the drone’s egocentric view
 <p>
 <img src="./assets/images/dataset_concept.png" alt="DatasetConcept">
 </p>

 <h1 id="motivation">Motivation</h1>
With the advent of low-cost commercial mini-UAVs, new applications and ways of interactions have emerged.
However, most of the existing UAV related dataset do not target such applications, prohibiting the development of data-driven methods.
Towards that end, we introduce UAVA a dataset designed for facilitating the development of such methods.
The dataset was created by leveraging an existing photorealistic dataset of indoor scenes, and by following a carefully designed gamification approach.

<h1>Trajectories</h1>
For collecting realistic and unbiased trajectories, we developed a game on <a href="https://unity.com/">Unity3D</a> and <a href="https://microsoft.github.io/AirSim/">AirSim</a>.
Collectible cube “coins” were placed at each of the known panorama positions (anchors) players were forced to navigate within the whole scene to collect the coins.
We record the drone's world pose among the scene at each time step.

<img src="./assets/videos/Unity_game.gif" alt="Gamification">


<h1> Modalities </h1>
For the egocentric "UAV" view we generate using <a href="https://www.blender.org/">Blender</a> ,colour images, depth, and surface maps, in addition to the optical ﬂow for two consecutive frames <b>t, t + 1 </b> sampled from the dense play-through trajectories.
For the exocentric "user" view apart from the afforementioned modalities we generated and drone's silhouette images.
<h2> Samples </h2>
<table>
<tr>
<td>
<img src="./assets/images/EgoSamples.png" alt="EgoSamples">
</td>
</tr>
<tr>
<td>
<img src="./assets/images/ExoSamples.png" alt="ExoSamples">
</td>
</tr>
</table>

 <h1> Usage </h1>

 <h2> Download </h2>
<p>We follow a <b>two-step</b> procedure to download the <b>UAVA</b> dataset.</p>

<p style="text-align: justify;">
<ol>
  <li>
    Access to UAVA dataset requires to agree with the terms and conditions for each of the 3D datasets that were used to create (i.e. render) it. Therefore, in order to grant you access to this dataset, we need to you to first fill <a href="https://forms.gle/uCAZutW8PGzR8Mhn9">this request form.</a>
  </li>
  <li>
    Then you need to perform request for access to Zenodo, the data hosting portal for the UAVA dataset. Due to data-size limitations and future dataset enhancements (e.g addition of new drone mdoels, etc.), the dataset is split per drone model, camera view, and modalities into seperate volumes.
    The first volumes contains the M2ED drone model, and  data from different views.
    In more detail the first link contains colour, depth , and silhouette of the drone from an exocentric view <a href="https://zenodo.org/record/3407840#.XX06KygzaUk"></a>
    The second link contains colour and depth data from the egocentric (i.e. UAV view)
    which respectively contain the <a href="https://zenodo.org/record/3407840#.XX06KygzaUk"></a> (<i>i.e.</i> Left-Down), <a href="https://zenodo.org/record/3407875#.XX08HCgzaUk">Right</a> and <a href="https://zenodo.org/record/3408441#.XX1QWCgzaUk">Up</a> viewpoints respectively. 
    Therefore, a separate request for access needs to be made for each viewpoint to the corresponding Zenodo repository.
  </li>
</ol>
</p>
<p style="text-align: justify;">
  <b>Note</b> that only completing one step of the two (<i>i.e.</i> only filling out the form, or only requesting access from the Zenodo repositories <b>will not</b> be enough to get access to the data. We will do our best to contact you in such cases and notify you to complete all steps as needed, but our mails may be lost (e.g. spam filters/folders). 
  The only exception to this, is if you have already filled in the form and need access to another Zenodo repository (for example you need extra viewpoint renders which are hosted on different Zenodo repositories), then you only need to fill in the Zenodo request but please, make sure to mention that the form has already been filled in so that we can verify it.
</p>

<p style="text-align: justify;">
Each volume is broken down in several <code>.zip</code> files (2GB each) for more convinient downloading on low bandwidth connections. You need all the <code>.zip</code> archives of each volume in order to extract the containing files.
</p>
</p>
 <h2> Data splits </h2>
 We follow the same data-split logic as defined in Matterport3D.

  <h2> Data organisation</h2>
  
 <h1> Acknowledgements </h1>
 This dataset has been generated within the European Union’s Horizon 2020 innovation programme [FASTER](https://www.faster-project.eu/) under grant agreement No 833507.

 <table>
<tr>
<td>
<img src="./assets/images/eu.png" alt="eu">
</td>
<td>
<img src="./assets/images/faster.png" alt="faster">
</td>
</tr>
</table>
