/**
 * RealTrace AI — AI Awareness, Deepfake Literacy & Indian Cyber Grievance Directory
 * Interactive client-side logic: State Directory Search, Incident Assistant, Quiz Game, Audio FX
 */

// ----------------------------------------------------------------------------
// 1. STATE-WISE INDIAN CYBER CRIME POLICE CELLS DIRECTORY DATA (36 States & UTs)
// ----------------------------------------------------------------------------
const INDIAN_CYBER_CELLS = [
  {
    state: "Delhi (NCT)",
    agency: "Delhi Police IFSO (Special Cell) & Cyber Crime Unit",
    phone: "1930 / 011-20892633",
    email: "cybercrime-delhi@nic.in",
    portal: "https://delhipolice.gov.in",
    location: "Dwarka Sector 19, New Delhi",
    category: "Metropolitan"
  },
  {
    state: "Maharashtra",
    agency: "Maharashtra Cyber (Mahacyber HQ) & Mumbai Cyber Police",
    phone: "1930 / 022-22160080",
    email: "sp.cbr-mah@gov.in",
    portal: "https://mahacyber.gov.in",
    location: "World Trade Centre, Cuffe Parade, Mumbai",
    category: "Western"
  },
  {
    state: "Karnataka",
    agency: "CID Cyber Crime Police Station & Bengaluru Cyber Command",
    phone: "1930 / 080-22201026",
    email: "comp-cyber-cid@karnataka.gov.in",
    portal: "https://ksp.karnataka.gov.in",
    location: "Carlton House, Palace Road, Bengaluru",
    category: "Southern"
  },
  {
    state: "Telangana",
    agency: "Telangana Cyber Security Bureau (TGCSB)",
    phone: "1930 / 040-27852445",
    email: "sp-cybercrimes-cid@tspolice.gov.in",
    portal: "https://tspolice.gov.in",
    location: "DGP Office Complex, Lakdikapool, Hyderabad",
    category: "Southern"
  },
  {
    state: "Tamil Nadu",
    agency: "Cyber Crime Wing (CCW) - Tamil Nadu Police",
    phone: "1930 / 044-28447701",
    email: "cybercrime.tnpolice@gov.in",
    portal: "https://eservices.tnpolice.gov.in",
    location: "Police Headquarters, Radhakrishnan Salai, Chennai",
    category: "Southern"
  },
  {
    state: "Uttar Pradesh",
    agency: "UP Cyber Crime Police Headquarters & 18 Range Cyber Thanas",
    phone: "1930 / 0522-2200234",
    email: "sp-cyber.lu@up.gov.in",
    portal: "https://uppolice.gov.in",
    location: "Signature Building, Gomti Nagar Extension, Lucknow",
    category: "Northern"
  },
  {
    state: "Gujarat",
    agency: "Gujarat CID Crime State Cyber Crime Cell",
    phone: "1930 / 079-23254395",
    email: "cc-cid@gujarat.gov.in",
    portal: "https://police.gujarat.gov.in",
    location: "CID Crime Bhavan, Sector 18, Gandhinagar",
    category: "Western"
  },
  {
    state: "West Bengal",
    agency: "CID West Bengal Cyber Crime PS & Kolkata Cyber Cell",
    phone: "1930 / 033-24795858",
    email: "cyber-cid@wb.gov.in",
    portal: "https://cidwestbengal.gov.in",
    location: "Bhabani Bhavan, Alipore, Kolkata",
    category: "Eastern"
  },
  {
    state: "Kerala",
    agency: "Kerala Police Cyber Crime Police Station (Cyberdome)",
    phone: "1930 / 0471-2313777",
    email: "cyberdome.pol@kerala.gov.in",
    portal: "https://keralapolice.gov.in",
    location: "Technopark Campus, Thiruvananthapuram",
    category: "Southern"
  },
  {
    state: "Rajasthan",
    agency: "Rajasthan State Cyber Crime Police Station",
    phone: "1930 / 0141-2601955",
    email: "ccps-scrb-raj@nic.in",
    portal: "https://police.rajasthan.gov.in",
    location: "SCRB Complex, Nehru Place, Tonk Road, Jaipur",
    category: "Northern"
  },
  {
    state: "Haryana",
    agency: "State Cyber Crime Police Station Haryana",
    phone: "1930 / 0172-2587538",
    email: "cyberps.scr-hry@gov.in",
    portal: "https://haryanapolice.gov.in",
    location: "Police Headquarters, Sector 6, Panchkula",
    category: "Northern"
  },
  {
    state: "Punjab",
    agency: "State Cyber Crime Division, Punjab Bureau of Investigation",
    phone: "1930 / 0172-2215286",
    email: "igp.cyber.pb@punjabpolice.gov.in",
    portal: "https://punjabpolice.gov.in",
    location: "Phase 4, SAS Nagar, Mohali",
    category: "Northern"
  },
  {
    state: "Bihar",
    agency: "Economic Offences Unit (EOU) Cyber Crime Cell",
    phone: "1930 / 0612-2215142",
    email: "sp-cyber-bih@nic.in",
    portal: "https://eou.bihar.gov.in",
    location: "Old Secretariat, Deshratna Marg, Patna",
    category: "Eastern"
  },
  {
    state: "Andhra Pradesh",
    agency: "AP CID Cyber Crime Police Station",
    phone: "1930 / 0863-2340100",
    email: "cybercrime-cid@ap.gov.in",
    portal: "https://cid.appolice.gov.in",
    location: "CID HQ, Near DGP Office, Mangalagiri, Guntur",
    category: "Southern"
  },
  {
    state: "Madhya Pradesh",
    agency: "State Cyber Police Headquarters Madhya Pradesh",
    phone: "1930 / 0755-2770248",
    email: "sp.cybercell@mppolice.gov.in",
    portal: "https://mppolice.gov.in",
    location: "Bhadbhada Road, Jahangirabad, Bhopal",
    category: "Central"
  },
  {
    state: "Odisha",
    agency: "Cyber Police Station, Crime Branch Odisha",
    phone: "1930 / 0671-2305485",
    email: "cyberps.od@nic.in",
    portal: "https://odishapolice.gov.in",
    location: "CID Crime Branch, Buxi Bazar, Cuttack",
    category: "Eastern"
  },
  {
    state: "Assam",
    agency: "CID Assam Cyber Crime Police Station",
    phone: "1930 / 0361-2462550",
    email: "cyberps-cid@assampolice.gov.in",
    portal: "https://police.assam.gov.in",
    location: "CID Complex, Ulubari, Guwahati",
    category: "North-Eastern"
  },
  {
    state: "Jammu & Kashmir",
    agency: "Cyber Police Station Kashmir & Jammu",
    phone: "1930 / 0194-2450570",
    email: "cyberpolice-jk@nic.in",
    portal: "https://jkpolice.gov.in",
    location: "Shergarhi, Srinagar / Bahu Plaza, Jammu",
    category: "Northern"
  },
  {
    state: "Jharkhand",
    agency: "Cyber Crime Police Station CID Jharkhand",
    phone: "1930 / 0651-2490046",
    email: "cyberps@jhpolice.gov.in",
    portal: "https://jhpolice.gov.in",
    location: "CID Headquarters, Doranda, Ranchi",
    category: "Eastern"
  },
  {
    state: "Chhattisgarh",
    agency: "State Cyber Crime Police Station Chhattisgarh",
    phone: "1930 / 0771-2511623",
    email: "cybercell-cg@nic.in",
    portal: "https://cgpolice.gov.in",
    location: "PHQ Complex, Sector 19, Nawa Raipur",
    category: "Central"
  },
  {
    state: "Uttarakhand",
    agency: "Special Task Force (STF) Cyber Crime Police Station",
    phone: "1930 / 0135-2655900",
    email: "ccps.stf-uk@nic.in",
    portal: "https://uttarakhandpolice.uk.gov.in",
    location: "Dalanwala, Dehradun",
    category: "Northern"
  },
  {
    state: "Himachal Pradesh",
    agency: "State Cyber Crime Police Station CID HP",
    phone: "1930 / 0177-2627955",
    email: "cyber-cid-hp@nic.in",
    portal: "https://hppolice.gov.in",
    location: "CID Headquarters, Kasumpti, Shimla",
    category: "Northern"
  },
  {
    state: "Goa",
    agency: "Goa Cyber Crime Police Station",
    phone: "1930 / 0832-2420883",
    email: "pi-cyber.goa@nic.in",
    portal: "https://citizen.goapolice.gov.in",
    location: "Ribandar Police Station Complex, Ribandar",
    category: "Western"
  },
  {
    state: "Chandigarh (UT)",
    agency: "Chandigarh Police Cyber Crime Investigation Cell (CCIC)",
    phone: "1930 / 0172-2746097",
    email: "cybercrime-chd@nic.in",
    portal: "https://chandigarhpolice.gov.in",
    location: "Sector 17 Police Station, Chandigarh",
    category: "Northern"
  },
  {
    state: "Tripura",
    agency: "Tripura State Cyber Crime Police Station",
    phone: "1930 / 0381-2324001",
    email: "cyberps-tr@nic.in",
    portal: "https://tripurapolice.gov.in",
    location: "Police Headquarters, Fire Brigade Chowmuhani, Agartala",
    category: "North-Eastern"
  },
  {
    state: "Meghalaya",
    agency: "Cyber Crime Police Station Meghalaya CID",
    phone: "1930 / 0364-2591402",
    email: "cyberps-meg@nic.in",
    portal: "https://megpolice.gov.in",
    location: "CID Complex, Mawroh, Shillong",
    category: "North-Eastern"
  },
  {
    state: "Manipur",
    agency: "Cyber Crime Police Station Manipur",
    phone: "1930 / 0385-2450159",
    email: "cybercrime-mn@nic.in",
    portal: "https://manipurpolice.gov.in",
    location: "CID Complex, Imphal",
    category: "North-Eastern"
  },
  {
    state: "Nagaland",
    agency: "State Cyber Crime Police Station Nagaland",
    phone: "1930 / 0370-2244275",
    email: "cybercrime-ngl@nic.in",
    portal: "https://police.nagaland.gov.in",
    location: "PHQ Complex, Kohima",
    category: "North-Eastern"
  },
  {
    state: "Mizoram",
    agency: "Cyber Crime Police Station Mizoram CID",
    phone: "1930 / 0389-2334478",
    email: "cyberps-miz@nic.in",
    portal: "https://police.mizoram.gov.in",
    location: "CID Complex, Khatla, Aizawl",
    category: "North-Eastern"
  },
  {
    state: "Arunachal Pradesh",
    agency: "Special Investigation Team (SIT) Cyber Crime Cell",
    phone: "1930 / 0360-2212233",
    email: "sit-cyber-arn@nic.in",
    portal: "https://arunpol.nic.in",
    location: "Police Headquarters, Itanagar",
    category: "North-Eastern"
  },
  {
    state: "Sikkim",
    agency: "Cyber Crime Police Station Sikkim CID",
    phone: "1930 / 03592-202087",
    email: "cybercrime-sik@nic.in",
    portal: "https://sikkimpolice.nic.in",
    location: "Police Headquarters, Gangtok",
    category: "North-Eastern"
  },
  {
    state: "Puducherry (UT)",
    agency: "Puducherry Cyber Crime Police Station",
    phone: "1930 / 0413-2277444",
    email: "cybercell-py@nic.in",
    portal: "https://police.py.gov.in",
    location: "Dumas Street, White Town, Puducherry",
    category: "Southern"
  },
  {
    state: "Ladakh (UT)",
    agency: "Cyber Police Station Ladakh",
    phone: "1930 / 01982-252200",
    email: "cyberpolice-ladakh@nic.in",
    portal: "https://police.ladakh.gov.in",
    location: "District Police Lines, Leh",
    category: "Northern"
  },
  {
    state: "Andaman & Nicobar Islands (UT)",
    agency: "Cyber Crime Police Station Port Blair",
    phone: "1930 / 03192-232546",
    email: "cybercell.andaman@nic.in",
    portal: "https://police.andaman.gov.in",
    location: "Aberdeen Bazaar, Port Blair",
    category: "Islands"
  }
];

// ----------------------------------------------------------------------------
// 2. INTERACTIVE SPOT-THE-FAKE CHALLENGE DATA
// ----------------------------------------------------------------------------
const QUIZ_QUESTIONS = [
  {
    id: 1,
    title: "Scenario 1: Executive Portrait",
    scenarioDescription: "A profile image sent in an urgent LinkedIn connection request claiming to be an overseas CEO offering immediate high-paying remote employment.",
    optionA: {
      type: "synthetic",
      label: "Profile Photo A (AI-Generated)",
      imgBadge: "Midjourney v6.0 Synthetic",
      flaws: [
        "Mismatched specular corneal reflections in the left and right eyes.",
        "Earrings have completely different geometry on each ear lobe.",
        "Hair strands abruptly dissolve into background wall without natural follicle roots."
      ]
    },
    optionB: {
      type: "authentic",
      label: "Profile Photo B (Authentic Camera)",
      imgBadge: "Canon 5D Mk IV Optical Capture",
      flaws: [
        "Consistent depth-of-field blur with coherent circular bokeh discs.",
        "Natural skin pore distribution and micro-wrinkles matching light source."
      ]
    },
    correctAnswer: "A",
    explanation: "Photo A is AI-generated! Generative diffusion models synthesize face halves quasi-independently, almost always creating mismatched pupil shapes and asymmetrical ear jewelry."
  },
  {
    id: 2,
    title: "Scenario 2: Breaking News Incident Photo",
    scenarioDescription: "A viral photograph circulating on WhatsApp groups alleging a sudden bridge collapse in an Indian metropolitan city during heavy rain.",
    optionA: {
      type: "authentic",
      label: "News Image A (Authentic)",
      imgBadge: "Verified Press Photo",
      flaws: [
        "Legible, consistent street signs, vehicle number plates, and shop hoardings.",
        "Natural raindrops scattering specular street light consistently."
      ]
    },
    optionB: {
      type: "synthetic",
      label: "News Image B (AI-Generated)",
      imgBadge: "Flux.1 Generative Scene",
      flaws: [
        "Background street signs feature alien, unintelligible glyphs rather than Hindi or English words.",
        "Automobile wheels have deformed, impossible rim spoke geometries.",
        "Water puddles show reflections that do not align with foreground objects."
      ]
    },
    correctAnswer: "B",
    explanation: "Image B is AI-generated! Even modern generators fail at coherent typography in the background and frequently warp complex repetitive geometries like wheel rims and pedestrian limbs."
  },
  {
    id: 3,
    title: "Scenario 3: Video KYC Call Screenshot",
    scenarioDescription: "A screenshot received during a video call where a caller in police uniform claims you are placed under 'Digital Arrest' for customs contraband.",
    optionA: {
      type: "synthetic",
      label: "Video Call Frame A (Deepfake Impersonator)",
      imgBadge: "Real-time Face-Swap Stream",
      flaws: [
        "Noticeable boundary blur around the collar and jawline where the swapped face is pasted.",
        "The police insignia and national emblem on the shoulder badge are distorted and blurred.",
        "Eye blinking is either unnaturally absent or unnaturally rapid without natural brow movement."
      ]
    },
    optionB: {
      type: "authentic",
      label: "Video Call Frame B (Natural Studio)",
      imgBadge: "Natural Web Camera",
      flaws: [
        "Natural motion blur consistent with shutter speed.",
        "Crisp uniform text and authentic government room insignia."
      ]
    },
    correctAnswer: "A",
    explanation: "Frame A is a deepfake live face-swap! Police badges, room emblems, and collar boundaries reveal severe interpolation artifacts. Remember: Indian Law Enforcement NEVER conducts 'Digital Arrests' or video call courts!"
  },
  {
    id: 4,
    title: "Scenario 4: Hands & Fine Anatomy Inspection",
    scenarioDescription: "A close-up promotional image of a hands-on tech product demonstration.",
    optionA: {
      type: "synthetic",
      label: "Hand Photo A (AI-Generated)",
      imgBadge: "Stable Diffusion XL 1.0",
      flaws: [
        "Subject has 6 fingers on the right hand with an impossible extra knuckle joint.",
        "Fingernails have no cuticles and merge directly into the flesh.",
        "Watch strap clasp does not connect physically to the casing."
      ]
    },
    optionB: {
      type: "authentic",
      label: "Hand Photo B (Authentic)",
      imgBadge: "Sony A7S Optical Shot",
      flaws: [
        "Accurate 5-finger skeletal biomechanics.",
        "Realistic skin tension, knuckle creases, and cuticle lines."
      ]
    },
    correctAnswer: "A",
    explanation: "Photo A is an obvious AI fake! Hands remain one of the most reliable visual telltales due to complex 3D articulation that 2D diffusion models struggle to render consistently."
  }
];

// ----------------------------------------------------------------------------
// 3. SOUND EFFECTS SYNTHESIZER (Web Audio API — 0 dependencies, works offline)
// ----------------------------------------------------------------------------
class CyberAudioEngine {
  constructor() {
    this.ctx = null;
    this.enabled = localStorage.getItem("realtrace_audio_enabled") === "true";
  }

  init() {
    if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
    }
  }

  toggle() {
    this.enabled = !this.enabled;
    localStorage.setItem("realtrace_audio_enabled", this.enabled);
    if (this.enabled) {
      this.init();
      this.playSuccessTone();
    }
    return this.enabled;
  }

  playClick() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = "sine";
    osc.frequency.setValueAtTime(800, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(400, this.ctx.currentTime + 0.05);
    gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.05);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.05);
  }

  playSuccessTone() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    [523.25, 659.25, 783.99, 1046.5].forEach((freq, i) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, now + i * 0.06);
      gain.gain.setValueAtTime(0.06, now + i * 0.06);
      gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.06 + 0.15);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now + i * 0.06);
      osc.stop(now + i * 0.06 + 0.15);
    });
  }

  playAlertTone() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    [320, 240].forEach((freq, i) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "sawtooth";
      osc.frequency.setValueAtTime(freq, now + i * 0.1);
      gain.gain.setValueAtTime(0.08, now + i * 0.1);
      gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.1 + 0.12);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now + i * 0.1);
      osc.stop(now + i * 0.1 + 0.12);
    });
  }
}

const audio = new CyberAudioEngine();

// ----------------------------------------------------------------------------
// 4. PARTICLE CONSTELLATION BACKGROUND
// ----------------------------------------------------------------------------
function initCyberParticles(canvasId = "cyber-particles") {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  let width = canvas.width = window.innerWidth;
  let height = canvas.height = window.innerHeight;

  const particles = [];
  const particleCount = Math.min(65, Math.floor((width * height) / 18000));

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.45,
      vy: (Math.random() - 0.5) * 0.45,
      radius: Math.random() * 1.8 + 0.6,
      alpha: Math.random() * 0.5 + 0.2
    });
  }

  let mouse = { x: null, y: null, maxDist: 120 };

  window.addEventListener("mousemove", (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY + window.scrollY;
  });

  window.addEventListener("mouseleave", () => {
    mouse.x = null;
    mouse.y = null;
  });

  window.addEventListener("resize", () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  function render() {
    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < particles.length; i++) {
      const p = particles[i];
      p.x += p.vx;
      p.y += p.vy;

      if (p.x < 0) p.x = width;
      if (p.x > width) p.x = 0;
      if (p.y < 0) p.y = height;
      if (p.y > height) p.y = 0;

      // Draw particle
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(139, 92, 246, ${p.alpha})`;
      ctx.fill();

      // Connect near particles
      for (let j = i + 1; j < particles.length; j++) {
        const p2 = particles[j];
        const dx = p.x - p2.x;
        const dy = p.y - p2.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 110) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.strokeStyle = `rgba(139, 92, 246, ${0.18 * (1 - dist / 110)})`;
          ctx.lineWidth = 0.7;
          ctx.stroke();
        }
      }
    }

    requestAnimationFrame(render);
  }

  render();
}

// ----------------------------------------------------------------------------
// 5. TOAST NOTIFICATION UTILITY
// ----------------------------------------------------------------------------
function showToast(message, type = "success") {
  const existing = document.getElementById("cyber-toast");
  if (existing) existing.remove();

  const toast = document.createElement("div");
  toast.id = "cyber-toast";
  toast.className = `fixed bottom-6 right-6 z-50 px-4 py-3 rounded-xl backdrop-blur-md shadow-2xl flex items-center gap-3 border text-xs sm:text-sm font-medium transition-all transform duration-300 translate-y-4 opacity-0 ${
    type === "success" 
      ? "bg-[#0f1923]/95 border-emerald-500/40 text-emerald-300 shadow-emerald-500/20" 
      : "bg-[#1f0f16]/95 border-rose-500/40 text-rose-300 shadow-rose-500/20"
  }`;

  const iconName = type === "success" ? "check-circle" : "alert-triangle";
  toast.innerHTML = `
    <i data-lucide="${iconName}" class="w-4 h-4 flex-shrink-0"></i>
    <span>${message}</span>
  `;
  document.body.appendChild(toast);
  lucide.createIcons();

  requestAnimationFrame(() => {
    toast.classList.remove("translate-y-4", "opacity-0");
  });

  setTimeout(() => {
    toast.classList.add("translate-y-4", "opacity-0");
    setTimeout(() => toast.remove(), 300);
  }, 2800);
}

function copyToClipboard(text, label = "Item") {
  audio.playClick();
  navigator.clipboard.writeText(text).then(() => {
    showToast(`${label} copied to clipboard!`, "success");
  }).catch(() => {
    showToast(`Failed to copy to clipboard`, "error");
  });
}

// ----------------------------------------------------------------------------
// 6. STATE POLICE DIRECTORY RENDERING & SEARCH
// ----------------------------------------------------------------------------
function renderStateDirectory(filterQuery = "", categoryFilter = "All") {
  const container = document.getElementById("state-directory-grid");
  const countBadge = document.getElementById("state-results-count");
  if (!container) return;

  const query = filterQuery.toLowerCase().trim();
  const filtered = INDIAN_CYBER_CELLS.filter(item => {
    const matchesQuery = item.state.toLowerCase().includes(query) ||
                         item.agency.toLowerCase().includes(query) ||
                         item.location.toLowerCase().includes(query) ||
                         item.phone.toLowerCase().includes(query) ||
                         item.email.toLowerCase().includes(query);
    const matchesCat = categoryFilter === "All" || item.category === categoryFilter;
    return matchesQuery && matchesCat;
  });

  if (countBadge) {
    countBadge.textContent = `${filtered.length} of ${INDIAN_CYBER_CELLS.length} States & UTs`;
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="col-span-full glass-card p-12 text-center">
        <i data-lucide="search-x" class="w-12 h-12 text-gray-500 mx-auto mb-3"></i>
        <h4 class="text-base font-bold text-white">No State Cyber Cells Found</h4>
        <p class="text-xs text-gray-400 mt-1">Try adjusting your search terms or dial the central 24x7 helpline: <strong class="text-rose-400">1930</strong>.</p>
      </div>
    `;
    lucide.createIcons();
    return;
  }

  container.innerHTML = filtered.map(item => `
    <div class="glass-card p-5 flex flex-col justify-between hover:border-purple-500/40 transition-all group">
      <div>
        <div class="flex items-center justify-between gap-2 mb-2">
          <span class="text-xs font-bold text-purple-400 group-hover:text-purple-300 transition-colors flex items-center gap-1.5">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 text-purple-400"></i>
            <span>${item.state}</span>
          </span>
          <span class="text-[10px] uppercase font-semibold px-2 py-0.5 rounded bg-white/5 text-gray-400 border border-white/10">
            ${item.category}
          </span>
        </div>

        <h4 class="text-sm font-bold text-white mb-2 leading-snug">${item.agency}</h4>
        
        <p class="text-[11px] text-gray-400 mb-3 flex items-start gap-1.5">
          <i data-lucide="building" class="w-3.5 h-3.5 text-gray-500 flex-shrink-0 mt-0.5"></i>
          <span>${item.location}</span>
        </p>

        <div class="space-y-2 text-xs font-mono bg-white/[0.02] p-3 rounded-lg border border-white/5 mb-4">
          <div class="flex items-center justify-between gap-2">
            <div class="flex items-center gap-1.5 truncate text-gray-300">
              <i data-lucide="phone" class="w-3 h-3 text-emerald-400 flex-shrink-0"></i>
              <span class="truncate">${item.phone}</span>
            </div>
            <button type="button" class="text-gray-400 hover:text-emerald-400 transition-colors p-1" onclick="copyToClipboard('${item.phone}', '${item.state} Phone')" title="Copy Phone">
              <i data-lucide="copy" class="w-3 h-3"></i>
            </button>
          </div>

          <div class="flex items-center justify-between gap-2">
            <div class="flex items-center gap-1.5 truncate text-gray-300">
              <i data-lucide="mail" class="w-3 h-3 text-purple-400 flex-shrink-0"></i>
              <span class="truncate">${item.email}</span>
            </div>
            <button type="button" class="text-gray-400 hover:text-purple-400 transition-colors p-1" onclick="copyToClipboard('${item.email}', '${item.state} Email')" title="Copy Email">
              <i data-lucide="copy" class="w-3 h-3"></i>
            </button>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-2 pt-2 border-t border-white/10 text-xs">
        <a href="tel:${item.phone.split('/')[0].trim()}" class="py-2 rounded-lg bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/25 text-emerald-300 font-semibold text-center transition-all flex items-center justify-center gap-1.5">
          <i data-lucide="phone-call" class="w-3 h-3"></i>
          <span>Call</span>
        </a>
        <a href="${item.portal}" target="_blank" rel="noopener" class="py-2 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-gray-200 font-semibold text-center transition-all flex items-center justify-center gap-1.5">
          <span>Official Portal</span>
          <i data-lucide="external-link" class="w-3 h-3 text-gray-400"></i>
        </a>
      </div>
    </div>
  `).join("");

  lucide.createIcons();
}

// ----------------------------------------------------------------------------
// 7. INCIDENT ASSISTANT & AUTO-COMPLAINT DRAFT GENERATOR
// ----------------------------------------------------------------------------
const INCIDENT_CONFIGS = {
  "financial": {
    title: "Financial Phishing & Unauthorized UPI / Bank Transfer",
    helpline: "Dial 1930 Immediately",
    legalSection: "Section 66D IT Act & Section 318 BNS (Cheating & Impersonation)",
    immediateSteps: [
      "Dial 1930 within the 'Golden Hour' (first 2-3 hours) so I4C can freeze funds in the suspect's mule bank account.",
      "Call your bank customer care immediately to block debit cards, internet banking, and compromised UPI IDs.",
      "Preserve bank SMS alerts, UTR numbers, UPI transaction reference IDs, and payment screenshots.",
      "File formal complaint at cybercrime.gov.in under 'Financial Fraud' category."
    ],
    evidenceNeeded: ["Bank Statement with transaction highlighted", "SMS debit alerts", "Suspect UPI ID / Mobile number", "Screenshots of deceptive link / WhatsApp chat"],
    template: (data) => `To,\nThe Officer-in-Charge,\nCyber Crime Police Station / National Cyber Crime Reporting Portal,\n\nSubject: Formal Complaint regarding Unauthorized Financial Cyber Fraud amounting to Rs. ${data.amount || '[Amount]'}.\n\nRespected Sir/Madam,\n\nI am writing to formally report an unauthorized financial cyber crime committed against me on ${data.date || '[Date/Time]'}.\n\nBrief Summary of Incident:\nI received a fraudulent communication via ${data.platform || '[SMS/WhatsApp/Call]'} from the suspect using phone/account: ${data.suspectInfo || '[Suspect Phone/ID]'}.\n\nDetails of Unauthorized Transactions:\n1. Amount Debited: Rs. ${data.amount || '[Amount]'}\n2. Bank & Account: ${data.bank || '[Bank Name]'}\n3. Transaction / UTR Reference ID: ${data.utr || '[Transaction Reference ID]'}\n4. Date & Time of Transfer: ${data.date || '[Date & Time]'}\n\nImmediate Actions Taken:\nI have contacted my bank to lock further transactions and reported the matter to the National Cyber Helpline 1930.\n\nI request you to kindly register this complaint, trace the beneficiary accounts, and take necessary legal action under Section 66D of the Information Technology Act and applicable provisions of the Bharatiya Nyaya Sanhita (BNS).\n\nEnclosures:\n1. Copy of Bank Account Statement showing unauthorized debit.\n2. Screenshots of fraudulent communication and suspect phone number.\n3. Copy of Aadhaar / Identity proof.\n\nYours faithfully,\n[Your Full Name]\n[Contact Mobile Number]\n[Full Postal Address]`
  },
  "deepfake": {
    title: "Deepfake Image Morphing, Blackmail & Cyber Extortion",
    helpline: "Call 1930 / WhatsApp NCW: 7827170170",
    legalSection: "Section 66E, 67, 67A IT Act & Section 77, 308 BNS (Privacy Violation & Extortion)",
    immediateSteps: [
      "DO NOT pay extortion money. Blackmailers will demand more once money is sent.",
      "Preserve evidence immediately: Take complete uncropped screenshots of profile handles, chats, blackmail demands, and URLs.",
      "File complaint at cybercrime.gov.in under 'Report Crime Related to Women / Child' (option for anonymous filing available).",
      "Issue 24-hour takedown notice to social media platform grievance officer under IT Rules 2021 Rule 3(2)(b)."
    ],
    evidenceNeeded: ["Uncropped screenshots of chats with timestamps", "Suspect social media URLs / WhatsApp numbers", "The synthetic morphed media file (stored safely as evidence)", "Extortion money demands / crypto wallet / UPI requests"],
    template: (data) => `To,\nThe Grievance Officer / Cyber Crime Police Cell,\nNational Cyber Crime Reporting Portal (cybercrime.gov.in),\n\nSubject: Urgent Complaint regarding Non-Consensual Synthetic AI Morphing, Blackmail and Criminal Extortion.\n\nRespected Sir/Madam,\n\nI am lodging this urgent complaint regarding malicious creation and dissemination of synthetic AI-morphed / deepfake visual content violating my privacy and dignity.\n\nIncident Specifics:\n1. Date of incident / discovery: ${data.date || '[Date]'}\n2. Platform where synthetic media was uploaded/sent: ${data.platform || '[Instagram / WhatsApp / Telegram]'}\n3. Suspect Profile Handle / URL / Mobile: ${data.suspectInfo || '[Suspect Handle or Phone Number]'}\n4. Extortion Demands: ${data.amount ? 'Suspect demanded Rs. ' + data.amount : 'Suspect attempted extortion / harassment'}\n\nLegal Infringements:\nThis act constitutes gross criminal violation under:\n- Section 66E IT Act (Violation of Privacy)\n- Section 67 & 67A IT Act (Publishing obscene/sexually explicit content in electronic form)\n- Section 308 & 351 BNS (Extortion & Criminal Intimidation)\n- IT Rules 2021 Rule 3(2)(b) requiring 24-hour mandatory platform takedown.\n\nI request you to immediately register an FIR, mandate removal of this content across platforms, and trace the perpetrators.\n\nYours faithfully,\n[Name / Anonymous Victim Reference]\n[Contact Email / Phone]`
  },
  "digital_arrest": {
    title: "'Digital Arrest' Extortion Scam (Impersonating Police / CBI / ED)",
    helpline: "Dial 1930 / Dial 112 (Police Dispatch)",
    legalSection: "Section 66D IT Act & Section 204, 318 BNS (Impersonating Public Servant & Extortion)",
    immediateSteps: [
      "DISCONNECT the call immediately. Indian Law Enforcement, CBI, ED, and Judges NEVER conduct video arrests or online trials.",
      "NEVER transfer money into 'escrow accounts' or 'RBI verification accounts'—these are fraud mule accounts.",
      "Dial 1930 and inform state police at 112.",
      "Report suspect Skype, WhatsApp, or phone number to Chakshu portal (sancharsaathi.gov.in)."
    ],
    evidenceNeeded: ["Phone numbers / Skype IDs from which video call was received", "Call recordings or screenshots of fake police studio backdrop", "Bank account numbers provided by fraudster for fund transfers"],
    template: (data) => `To,\nThe Cyber Crime Investigation Cell / Central Bureau of Investigation,\n\nSubject: Complaint against Fraud Syndicate orchestrating 'Digital Arrest' Impersonation Scam.\n\nRespected Sir/Madam,\n\nI am writing to report a coercive cyber fraud operation attempting extortion through false impersonation of Indian law enforcement.\n\nDetails of Call:\n1. Date & Time: ${data.date || '[Date & Time]'}\n2. Call Platform: ${data.platform || '[WhatsApp Video / Skype / Mobile]'}\n3. Caller Mobile / Account: ${data.suspectInfo || '[Suspect Contact Info]'}\n4. False Claims Made: Caller claimed to represent CBI / Mumbai Police / Customs alleging a parcel with contraband / money laundering.\n5. Financial Demand: Demanded Rs. ${data.amount || '[Demanded Amount]'} under the pretext of 'RBI Verification Deposit'.\n\nI request you to track the SIM identity, investigate the bank accounts provided by the fraudsters, and initiate strict prosecution.\n\nYours faithfully,\n[Your Full Name]\n[Contact Number]`
  },
  "identity_theft": {
    title: "Identity Theft & Fake Social Profile Impersonation",
    helpline: "Report on Platform Grievance + cybercrime.gov.in",
    legalSection: "Section 66C & 66D IT Act (Identity Theft & Cheating by Personation)",
    immediateSteps: [
      "Notify friends and contacts on your real account not to respond to urgent money requests from the fake profile.",
      "Collect link and screenshot of the imposter profile.",
      "Submit an in-app impersonation report to the platform (Meta, Instagram, LinkedIn).",
      "File online cyber complaint at cybercrime.gov.in."
    ],
    evidenceNeeded: ["URL of the clone/imposter profile", "Screenshots showing stolen photos and bio", "Screenshots of any fraudulent requests sent to your friends"],
    template: (data) => `To,\nPlatform Grievance Officer & Cyber Crime Cell,\n\nSubject: Formal Complaint regarding Stolen Identity and Impersonation Profile.\n\nRespected Sir/Madam,\n\nAn unauthorized duplicate / fake account has been created using my stolen personal photos and name to deceive the public.\n\n1. Genuine Account URL: [Your Real Profile Link]\n2. Fake / Imposter Profile URL: ${data.suspectInfo || '[Imposter Link]'}\n3. Date Detected: ${data.date || '[Date]'}\n4. Platform: ${data.platform || '[Instagram / Facebook / LinkedIn]'}\n\nThis is a direct violation of Section 66C and 66D of the Information Technology Act. I request immediate suspension and termination of this fraudulent profile.\n\nYours faithfully,\n[Your Full Name]\n[Verified Phone/Email]`
  }
};

let currentIncidentKey = "financial";

function selectIncidentType(key) {
  audio.playClick();
  currentIncidentKey = key;

  document.querySelectorAll(".incident-type-btn").forEach(btn => {
    if (btn.dataset.type === key) {
      btn.classList.add("border-purple-500", "bg-purple-500/10", "text-purple-300");
      btn.classList.remove("border-white/10", "bg-white/5", "text-gray-300");
    } else {
      btn.classList.remove("border-purple-500", "bg-purple-500/10", "text-purple-300");
      btn.classList.add("border-white/10", "bg-white/5", "text-gray-300");
    }
  });

  updateIncidentOutput();
}

function updateIncidentOutput() {
  const config = INCIDENT_CONFIGS[currentIncidentKey];
  if (!config) return;

  const dateVal = document.getElementById("inc-date")?.value || "";
  const amountVal = document.getElementById("inc-amount")?.value || "";
  const platformVal = document.getElementById("inc-platform")?.value || "";
  const suspectVal = document.getElementById("inc-suspect")?.value || "";
  const bankVal = document.getElementById("inc-bank")?.value || "";
  const utrVal = document.getElementById("inc-utr")?.value || "";

  const data = {
    date: dateVal,
    amount: amountVal,
    platform: platformVal,
    suspectInfo: suspectVal,
    bank: bankVal,
    utr: utrVal
  };

  const stepsContainer = document.getElementById("inc-steps-container");
  if (stepsContainer) {
    stepsContainer.innerHTML = config.immediateSteps.map((step, idx) => `
      <li class="flex items-start gap-2.5 text-xs text-gray-300">
        <span class="w-5 h-5 rounded-full bg-rose-500/20 text-rose-400 font-bold text-[10px] flex items-center justify-center flex-shrink-0 mt-0.5">${idx + 1}</span>
        <span class="leading-relaxed">${step}</span>
      </li>
    `).join("");
  }

  const evidenceContainer = document.getElementById("inc-evidence-container");
  if (evidenceContainer) {
    evidenceContainer.innerHTML = config.evidenceNeeded.map(item => `
      <li class="flex items-center gap-2 text-xs text-purple-300">
        <i data-lucide="check-square" class="w-3.5 h-3.5 text-purple-400 flex-shrink-0"></i>
        <span>${item}</span>
      </li>
    `).join("");
  }

  const legalTag = document.getElementById("inc-legal-section");
  if (legalTag) {
    legalTag.textContent = config.legalSection;
  }

  const complaintDraft = document.getElementById("inc-complaint-draft");
  if (complaintDraft) {
    complaintDraft.value = config.template(data);
  }

  lucide.createIcons();
}

// ----------------------------------------------------------------------------
// 8. INTERACTIVE QUIZ ENGINE ("SPOT THE FAKE")
// ----------------------------------------------------------------------------
let currentQuizIndex = 0;
let userScore = 0;
let answeredQuestions = {};

function renderQuizQuestion(index) {
  const container = document.getElementById("quiz-card-container");
  if (!container) return;

  const q = QUIZ_QUESTIONS[index];
  const isAnswered = answeredQuestions[index] !== undefined;

  container.innerHTML = `
    <div class="glass-card p-6 sm:p-8">
      
      <div class="flex items-center justify-between mb-4">
        <div>
          <span class="text-[10px] font-bold uppercase tracking-wider text-purple-400 px-2 py-0.5 rounded bg-purple-500/10 border border-purple-500/20">Challenge ${index + 1} of ${QUIZ_QUESTIONS.length}</span>
          <h3 class="text-xl font-black text-white mt-1">${q.title}</h3>
        </div>
        <div class="text-right">
          <span class="text-xs text-gray-400 font-mono">Current Score:</span>
          <span class="text-lg font-black text-emerald-400 font-mono ml-1">${userScore}/${QUIZ_QUESTIONS.length}</span>
        </div>
      </div>

      <p class="text-xs sm:text-sm text-gray-300 mb-6 bg-white/[0.02] p-3 rounded-lg border border-white/5">
        <strong>Context:</strong> ${q.scenarioDescription}
      </p>

      <!-- Two Comparison Inspection Targets -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
        
        <!-- Option A -->
        <div id="quiz-opt-A" onclick="handleQuizAnswer('A')" class="quiz-option p-5 rounded-2xl border ${
          isAnswered 
            ? (q.correctAnswer === 'A' ? 'border-emerald-500 bg-emerald-500/10' : 'border-rose-500 bg-rose-500/10')
            : 'border-white/10 hover:border-purple-500 bg-white/5 hover:bg-white/10'
        } transition-all cursor-pointer relative group">
          
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-bold text-white flex items-center gap-2">
              <span class="w-6 h-6 rounded-full bg-white/10 group-hover:bg-purple-600 text-white font-mono text-xs flex items-center justify-center transition-colors">A</span>
              <span>Inspect Sample Option A</span>
            </span>
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-white/10 text-gray-300">${q.optionA.imgBadge}</span>
          </div>

          <div class="aspect-video rounded-xl bg-gradient-to-br from-indigo-950 via-purple-950 to-slate-950 border border-white/10 flex flex-col items-center justify-center p-4 text-center mb-3 group-hover:scale-[1.01] transition-transform">
            <i data-lucide="scan" class="w-8 h-8 text-purple-400 mb-2"></i>
            <span class="text-xs font-semibold text-gray-200">${q.optionA.label}</span>
            <span class="text-[10px] text-gray-400 mt-1">Click to Vote as AI Synthetic</span>
          </div>

          ${isAnswered ? `
            <div class="text-xs space-y-1.5 pt-3 border-t border-white/10">
              <strong class="text-purple-300 block text-[11px] uppercase font-bold">Forensic Markers:</strong>
              ${q.optionA.flaws.map(f => `<div class="text-[11px] text-gray-300 flex items-start gap-1.5"><i data-lucide="chevron-right" class="w-3 h-3 text-purple-400 mt-0.5 flex-shrink-0"></i><span>${f}</span></div>`).join("")}
            </div>
          ` : `
            <div class="text-center text-xs text-purple-300 font-semibold py-1">
              Tap to choose Option A as the AI Synthetic
            </div>
          `}
        </div>

        <!-- Option B -->
        <div id="quiz-opt-B" onclick="handleQuizAnswer('B')" class="quiz-option p-5 rounded-2xl border ${
          isAnswered 
            ? (q.correctAnswer === 'B' ? 'border-emerald-500 bg-emerald-500/10' : 'border-rose-500 bg-rose-500/10')
            : 'border-white/10 hover:border-purple-500 bg-white/5 hover:bg-white/10'
        } transition-all cursor-pointer relative group">
          
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-bold text-white flex items-center gap-2">
              <span class="w-6 h-6 rounded-full bg-white/10 group-hover:bg-purple-600 text-white font-mono text-xs flex items-center justify-center transition-colors">B</span>
              <span>Inspect Sample Option B</span>
            </span>
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-white/10 text-gray-300">${q.optionB.imgBadge}</span>
          </div>

          <div class="aspect-video rounded-xl bg-gradient-to-br from-slate-950 via-zinc-900 to-indigo-950 border border-white/10 flex flex-col items-center justify-center p-4 text-center mb-3 group-hover:scale-[1.01] transition-transform">
            <i data-lucide="camera" class="w-8 h-8 text-indigo-400 mb-2"></i>
            <span class="text-xs font-semibold text-gray-200">${q.optionB.label}</span>
            <span class="text-[10px] text-gray-400 mt-1">Click to Vote as AI Synthetic</span>
          </div>

          ${isAnswered ? `
            <div class="text-xs space-y-1.5 pt-3 border-t border-white/10">
              <strong class="text-indigo-300 block text-[11px] uppercase font-bold">Forensic Markers:</strong>
              ${q.optionB.flaws.map(f => `<div class="text-[11px] text-gray-300 flex items-start gap-1.5"><i data-lucide="chevron-right" class="w-3 h-3 text-indigo-400 mt-0.5 flex-shrink-0"></i><span>${f}</span></div>`).join("")}
            </div>
          ` : `
            <div class="text-center text-xs text-purple-300 font-semibold py-1">
              Tap to choose Option B as the AI Synthetic
            </div>
          `}
        </div>

      </div>

      <!-- Feedback Banner (when answered) -->
      ${isAnswered ? `
        <div class="p-4 rounded-xl ${answeredQuestions[index] === q.correctAnswer ? 'bg-emerald-500/10 border border-emerald-500/30' : 'bg-rose-500/10 border border-rose-500/30'} mb-6">
          <div class="flex items-center gap-2 mb-1">
            <i data-lucide="${answeredQuestions[index] === q.correctAnswer ? 'check-circle' : 'alert-circle'}" class="w-4 h-4 ${answeredQuestions[index] === q.correctAnswer ? 'text-emerald-400' : 'text-rose-400'}"></i>
            <span class="text-xs font-bold ${answeredQuestions[index] === q.correctAnswer ? 'text-emerald-300' : 'text-rose-300'}">
              ${answeredQuestions[index] === q.correctAnswer ? 'Correct Forensic Deduction!' : 'Incorrect Deduction'}
            </span>
          </div>
          <p class="text-xs text-gray-300 leading-relaxed">${q.explanation}</p>
        </div>
      ` : ''}

      <!-- Pagination / Next Controls -->
      <div class="flex items-center justify-between pt-4 border-t border-white/10">
        <button type="button" onclick="navigateQuiz(-1)" ${index === 0 ? 'disabled' : ''} class="px-4 py-2 rounded-lg bg-white/5 hover:bg-white/10 disabled:opacity-30 disabled:cursor-not-allowed text-xs font-semibold text-gray-300 transition-colors flex items-center gap-1.5">
          <i data-lucide="chevron-left" class="w-3.5 h-3.5"></i>
          <span>Previous</span>
        </button>

        <div class="flex items-center gap-1.5">
          ${QUIZ_QUESTIONS.map((_, i) => `
            <button type="button" onclick="goToQuiz(${i})" class="w-2.5 h-2.5 rounded-full transition-all ${
              i === index ? 'bg-purple-500 w-6' : (answeredQuestions[i] !== undefined ? 'bg-emerald-400' : 'bg-white/20')
            }"></button>
          `).join("")}
        </div>

        <button type="button" onclick="navigateQuiz(1)" ${index === QUIZ_QUESTIONS.length - 1 ? 'disabled' : ''} class="px-4 py-2 rounded-lg bg-purple-600 hover:bg-purple-700 disabled:opacity-30 disabled:cursor-not-allowed text-xs font-semibold text-white transition-colors flex items-center gap-1.5">
          <span>Next</span>
          <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
        </button>
      </div>

    </div>
  `;

  lucide.createIcons();
}

function handleQuizAnswer(selectedOption) {
  if (answeredQuestions[currentQuizIndex] !== undefined) return;

  const q = QUIZ_QUESTIONS[currentQuizIndex];
  answeredQuestions[currentQuizIndex] = selectedOption;

  if (selectedOption === q.correctAnswer) {
    userScore++;
    audio.playSuccessTone();
    showToast("Spot-on! You spotted the synthetic artifacts.", "success");
  } else {
    audio.playAlertTone();
    showToast("Careful! High-frequency AI flaws were in option " + q.correctAnswer, "error");
  }

  renderQuizQuestion(currentQuizIndex);
}

function navigateQuiz(delta) {
  audio.playClick();
  const next = currentQuizIndex + delta;
  if (next >= 0 && next < QUIZ_QUESTIONS.length) {
    currentQuizIndex = next;
    renderQuizQuestion(currentQuizIndex);
  }
}

function goToQuiz(idx) {
  audio.playClick();
  currentQuizIndex = idx;
  renderQuizQuestion(currentQuizIndex);
}

// ----------------------------------------------------------------------------
// 9. EVENT LISTENERS & INITIALIZATION
// ----------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", () => {
  // Initialize particles
  initCyberParticles("cyber-particles");

  // Initialize Audio button state
  const audioToggleBtn = document.getElementById("audio-toggle-btn");
  const audioIcon = document.getElementById("audio-icon");
  if (audioToggleBtn && audioIcon) {
    const updateAudioIcon = () => {
      audioIcon.setAttribute("data-lucide", audio.enabled ? "volume-2" : "volume-x");
      audioToggleBtn.title = audio.enabled ? "Mute Cyber Audio FX" : "Enable Cyber Audio FX";
      lucide.createIcons();
    };
    updateAudioIcon();

    audioToggleBtn.addEventListener("click", () => {
      const enabled = audio.toggle();
      updateAudioIcon();
      showToast(enabled ? "Sound FX Enabled" : "Sound FX Muted", "success");
    });
  }

  // Render State Directory
  renderStateDirectory();

  const searchInput = document.getElementById("state-search-input");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      const cat = document.querySelector(".state-filter-pill.active")?.dataset.category || "All";
      renderStateDirectory(e.target.value, cat);
    });
  }

  // Category filter buttons
  document.querySelectorAll(".state-filter-pill").forEach(pill => {
    pill.addEventListener("click", () => {
      audio.playClick();
      document.querySelectorAll(".state-filter-pill").forEach(p => {
        p.classList.remove("active", "bg-purple-600", "text-white");
        p.classList.add("bg-white/5", "text-gray-400");
      });
      pill.classList.add("active", "bg-purple-600", "text-white");
      pill.classList.remove("bg-white/5", "text-gray-400");

      const query = document.getElementById("state-search-input")?.value || "";
      renderStateDirectory(query, pill.dataset.category);
    });
  });

  // Incident Type buttons
  document.querySelectorAll(".incident-type-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      selectIncidentType(btn.dataset.type);
    });
  });

  // Form field changes for Incident Assistant
  ["inc-date", "inc-amount", "inc-platform", "inc-suspect", "inc-bank", "inc-utr"].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener("input", updateIncidentOutput);
  });

  // Copy Complaint Draft button
  const copyComplaintBtn = document.getElementById("copy-complaint-btn");
  if (copyComplaintBtn) {
    copyComplaintBtn.addEventListener("click", () => {
      const draft = document.getElementById("inc-complaint-draft")?.value || "";
      copyToClipboard(draft, "Official Police Complaint Draft");
    });
  }

  // Render Quiz
  renderQuizQuestion(0);

  // Mobile menu toggle
  const mobileMenuBtn = document.getElementById("mobile-menu-btn");
  const mobileMenuDrawer = document.getElementById("mobile-menu-drawer");
  if (mobileMenuBtn && mobileMenuDrawer) {
    mobileMenuBtn.addEventListener("click", () => {
      audio.playClick();
      mobileMenuDrawer.classList.toggle("hidden");
    });
  }

  // Initial icons refresh
  lucide.createIcons();
});
