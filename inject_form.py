import re
import os

f_name = 'pre-inscription.html'

with open(f_name, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the entire <form> ... </form> tag and the progress stepper with a fully functional one.
# First, let's locate the <main> block entirely.

# The main block starts around <main class="flex-grow py-8 px-4 sm:px-6 lg:px-8">
# Let's write the whole <main> content out.

main_replacement = """<main class="flex-grow py-8 px-4 sm:px-6 lg:px-8">
<div class="max-w-[1100px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8">
<!-- Left Column: Form & Progress -->
<div class="lg:col-span-8 flex flex-col gap-6">
<!-- Title Section -->
<div class="bg-white dark:bg-[#1a2c2b] p-6 rounded-xl shadow-sm border border-slate-100 dark:border-slate-800">
<h2 class="text-2xl sm:text-3xl font-black text-secondary dark:text-white tracking-tight mb-2">Pré-inscription en ligne</h2>
<p class="text-slate-500 dark:text-slate-400">Année académique 2024-2025 • Licence &amp; Master</p>
</div>

<!-- Progress Stepper -->
<div class="bg-white dark:bg-[#1a2c2b] p-6 rounded-xl shadow-sm border border-slate-100 dark:border-slate-800 overflow-x-auto">
<div class="flex items-center justify-between min-w-[600px]" id="stepper">
    <!-- Step 1 -->
    <div class="flex flex-col items-center gap-2 relative z-10 w-32 group" data-step="1">
        <div class="step-circle size-10 rounded-full bg-primary flex items-center justify-center text-white font-bold shadow-[0_0_0_4px_rgba(25,215,202,0.2)] transition-all">1</div>
        <span class="step-label text-xs font-bold text-primary text-center">Infos Personnelles</span>
    </div>
    <div class="flex-1 h-1 bg-slate-100 dark:bg-slate-700 mx-2 rounded relative">
        <div class="step-line absolute left-0 top-0 h-full w-1/2 bg-gradient-to-r from-primary to-primary transition-all duration-300 rounded" id="line-1"></div>
    </div>
    <!-- Step 2 -->
    <div class="flex flex-col items-center gap-2 relative z-10 w-32 group opacity-60" data-step="2">
        <div class="step-circle size-8 rounded-full bg-slate-100 dark:bg-slate-800 border-2 border-slate-200 dark:border-slate-600 flex items-center justify-center text-slate-400 dark:text-slate-500 font-bold transition-all">2</div>
        <span class="step-label text-xs font-medium text-slate-500 dark:text-slate-400 text-center">Filière</span>
    </div>
    <div class="flex-1 h-1 bg-slate-100 dark:bg-slate-700 mx-2 rounded relative">
        <div class="step-line absolute left-0 top-0 h-full w-0 bg-gradient-to-r from-primary to-primary transition-all duration-300 rounded" id="line-2"></div>
    </div>
    <!-- Step 3 -->
    <div class="flex flex-col items-center gap-2 relative z-10 w-32 group opacity-60" data-step="3">
        <div class="step-circle size-8 rounded-full bg-slate-100 dark:bg-slate-800 border-2 border-slate-200 dark:border-slate-600 flex items-center justify-center text-slate-400 dark:text-slate-500 font-bold transition-all">3</div>
        <span class="step-label text-xs font-medium text-slate-500 dark:text-slate-400 text-center">Documents</span>
    </div>
    <div class="flex-1 h-1 bg-slate-100 dark:bg-slate-700 mx-2 rounded relative">
        <div class="step-line absolute left-0 top-0 h-full w-0 bg-gradient-to-r from-primary to-primary transition-all duration-300 rounded" id="line-3"></div>
    </div>
    <!-- Step 4 -->
    <div class="flex flex-col items-center gap-2 relative z-10 w-32 group opacity-60" data-step="4">
        <div class="step-circle size-8 rounded-full bg-slate-100 dark:bg-slate-800 border-2 border-slate-200 dark:border-slate-600 flex items-center justify-center text-slate-400 dark:text-slate-500 font-bold transition-all">4</div>
        <span class="step-label text-xs font-medium text-slate-500 dark:text-slate-400 text-center">Récapitulatif</span>
    </div>
</div>
</div>

<!-- Notice Web3Forms Integration -->
<div class="bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800 rounded-lg p-4 flex gap-3 text-sm text-blue-800 dark:text-blue-200 hidden" id="web3forms-notice">
    <span class="material-symbols-outlined text-blue-500 mt-0.5">info</span>
    <div>
        <strong>Remarque pour l'administrateur :</strong> Pour recevoir les emails, créez une clé Web3Forms via <a href="https://web3forms.com/" target="_blank" class="underline font-bold">web3forms.com</a> avec votre email <code>jmoussouami@icloud.com</code> et remplacez la valeur <code>YOUR_ACCESS_KEY_HERE</code> dans le code HTML. (Le formulaire est actuellement configuré pour la démonstration).
    </div>
</div>

<!-- Form Section -->
<form id="multi-step-form" class="flex flex-col gap-6" action="https://api.web3forms.com/submit" method="POST" enctype="multipart/form-data">
    
    <!-- Required Web3Forms Fields -->
    <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">
    <input type="hidden" name="subject" value="Nouvelle Pré-inscription USIH">
    <input type="hidden" name="redirect" value="https://web3forms.com/success">

    <!-- Step 1: Infos Personnelles -->
    <div class="form-step active" data-step="1">
        <div class="bg-white dark:bg-[#1a2c2b] rounded-xl shadow-lg border border-slate-100 dark:border-slate-800 overflow-hidden">
        <div class="p-6 border-b border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-800/30 flex justify-between items-center">
            <h3 class="text-lg font-bold text-secondary dark:text-white flex items-center gap-2">
                <span class="material-symbols-outlined text-primary">person</span> Informations Personnelles
            </h3>
            <span class="text-xs bg-primary/10 text-primary px-2 py-1 rounded font-bold">Étape 1/4</span>
        </div>
        <div class="p-6 sm:p-8 grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Nom -->
            <div class="space-y-2">
                <label class="block text-sm font-semibold text-slate-700 dark:text-slate-300">Nom de famille <span class="text-red-500">*</span></label>
                <input required class="w-full h-12 px-4 rounded-lg border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 focus:border-primary focus:ring-primary dark:text-white transition-all" id="lastname" name="lastname" placeholder="Ex: MOUSSAVOU" type="text"/>
            </div>
            <!-- Prénom -->
            <div class="space-y-2">
                <label class="block text-sm font-semibold text-slate-700 dark:text-slate-300">Prénoms <span class="text-red-500">*</span></label>
                <input required class="w-full h-12 px-4 rounded-lg border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 focus:border-primary focus:ring-primary dark:text-white transition-all" id="firstname" name="firstname" placeholder="Ex: Jean-Luc" type="text"/>
            </div>
            <!-- Date de naissance -->
            <div class="space-y-2">
                <label class="block text-sm font-semibold text-slate-700 dark:text-slate-300">Date de naissance <span class="text-red-500">*</span></label>
                <div class="relative">
                    <span class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 material-symbols-outlined text-[20px]">calendar_month</span>
                    <input required class="w-full h-12 pl-12 pr-4 rounded-lg border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 focus:border-primary focus:ring-primary dark:text-white transition-all text-slate-600 dark:text-slate-300" id="dob" name="dob" type="date"/>
                </div>
            </div>
            <!-- Nationalité -->
            <div class="space-y-2">
                <label class="block text-sm font-semibold text-slate-700 dark:text-slate-300">Nationalité <span class="text-red-500">*</span></label>
                <div class="relative">
                    <span class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 material-symbols-outlined text-[20px]">public</span>
                    <select required class="w-full h-12 pl-12 pr-4 rounded-lg border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 focus:border-primary focus:ring-primary dark:text-white transition-all text-slate-600 dark:text-slate-300 appearance-none" id="nationality" name="nationality">
                        <option value="" disabled selected>Sélectionner votre pays</option>
                        <option value="Gabon">Gabon</option>
                        <option value="France">France</option>
                        <option value="Sénégal">Sénégal</option>
                        <option value="Côte d'Ivoire">Côte d'Ivoire</option>
                        <option value="Cameroun">Cameroun</option>
                    </select>
                    <span class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-400 material-symbols-outlined text-[20px] pointer-events-none">expand_more</span>
                </div>
            </div>
            <!-- Email -->
            <div class="space-y-2 md:col-span-2">
                <label class="block text-sm font-semibold text-slate-700 dark:text-slate-300">Adresse Email <span class="text-red-500">*</span></label>
                <div class="relative">
                    <span class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 material-symbols-outlined text-[20px]">mail</span>
                    <input required class="w-full h-12 pl-12 pr-4 rounded-lg border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 focus:border-primary focus:ring-primary dark:text-white transition-all" id="email" name="email" placeholder="etudiant@exemple.com" type="email"/>
                </div>
            </div>
            <!-- Téléphone -->
            <div class="space-y-2 md:col-span-2">
                <label class="block text-sm font-semibold text-slate-700 dark:text-slate-300">Numéro de téléphone <span class="text-red-500">*</span></label>
                <div class="relative flex gap-2">
                    <select name="phone_prefix" class="h-12 w-24 rounded-lg border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 focus:border-primary focus:ring-primary dark:text-white text-sm font-medium">
                        <option value="+241">+241</option>
                        <option value="+33">+33</option>
                        <option value="+221">+221</option>
                    </select>
                    <input required class="flex-1 h-12 px-4 rounded-lg border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 focus:border-primary focus:ring-primary dark:text-white transition-all" id="phone" name="phone_number" placeholder="00 00 00 00" type="tel"/>
                </div>
            </div>
        </div>
        </div>
    </div>

    <!-- Step 2: Filière -->
    <div class="form-step hidden" data-step="2">
        <div class="bg-white dark:bg-[#1a2c2b] rounded-xl shadow-lg border border-slate-100 dark:border-slate-800 overflow-hidden">
        <div class="p-6 border-b border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-800/30 flex justify-between items-center">
            <h3 class="text-lg font-bold text-secondary dark:text-white flex items-center gap-2">
                <span class="material-symbols-outlined text-primary">school</span> Choix de la Filière
            </h3>
            <span class="text-xs bg-primary/10 text-primary px-2 py-1 rounded font-bold">Étape 2/4</span>
        </div>
        <div class="p-6 sm:p-8 flex flex-col gap-6">
            <div class="space-y-3">
                <label class="block text-sm font-semibold text-slate-700 dark:text-slate-300">Niveau d'étude souhaité <span class="text-red-500">*</span></label>
                <div class="flex flex-col sm:flex-row gap-4">
                    <label class="flex-1 relative">
                        <input type="radio" name="level" value="Licence" class="peer sr-only" required>
                        <div class="h-14 flex items-center px-4 border-2 border-slate-200 dark:border-slate-700 rounded-lg cursor-pointer peer-checked:border-primary peer-checked:bg-primary/5 transition-all">
                            <span class="font-bold text-slate-700 dark:text-white">Licence (Bac+3)</span>
                        </div>
                    </label>
                    <label class="flex-1 relative">
                        <input type="radio" name="level" value="Master" class="peer sr-only">
                        <div class="h-14 flex items-center px-4 border-2 border-slate-200 dark:border-slate-700 rounded-lg cursor-pointer peer-checked:border-primary peer-checked:bg-primary/5 transition-all">
                            <span class="font-bold text-slate-700 dark:text-white">Master (Bac+5)</span>
                        </div>
                    </label>
                </div>
            </div>
            <div class="space-y-2">
                <label class="block text-sm font-semibold text-slate-700 dark:text-slate-300">Domaine de formation <span class="text-red-500">*</span></label>
                <div class="relative">
                    <span class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 material-symbols-outlined text-[20px]">science</span>
                    <select required class="w-full h-12 pl-12 pr-4 rounded-lg border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 focus:border-primary focus:ring-primary dark:text-white transition-all text-slate-600 dark:text-slate-300 appearance-none" id="filiere" name="filiere">
                        <option value="" disabled selected>Sélectionner une filière</option>
                        <option value="Ingénierie Informatique">Ingénierie Informatique</option>
                        <option value="Génie Civil">Génie Civil</option>
                        <option value="Gestion & Management">Gestion & Management</option>
                        <option value="Sciences Énergétiques">Sciences Énergétiques</option>
                    </select>
                    <span class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-400 material-symbols-outlined text-[20px] pointer-events-none">expand_more</span>
                </div>
            </div>
        </div>
        </div>
    </div>

    <!-- Step 3: Documents -->
    <div class="form-step hidden" data-step="3">
        <div class="bg-white dark:bg-[#1a2c2b] rounded-xl shadow-lg border border-slate-100 dark:border-slate-800 overflow-hidden">
        <div class="p-6 border-b border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-800/30 flex justify-between items-center">
            <h3 class="text-lg font-bold text-secondary dark:text-white flex items-center gap-2">
                <span class="material-symbols-outlined text-primary">description</span> Documents Requis
            </h3>
            <span class="text-xs bg-primary/10 text-primary px-2 py-1 rounded font-bold">Étape 3/4</span>
        </div>
        <div class="p-6 sm:p-8 flex flex-col gap-6">
            <p class="text-sm text-slate-500 dark:text-slate-400">Veuillez uploader les documents suivants au format PDF ou JPG (Max 5Mo par fichier).</p>
            
            <div class="border-2 border-dashed border-slate-200 dark:border-slate-700 rounded-lg p-6 text-center hover:border-primary transition-colors bg-slate-50 dark:bg-slate-900/50">
                <input type="file" id="doc_bac" name="doc_bac" accept=".pdf,.jpg,.png" class="hidden">
                <label for="doc_bac" class="cursor-pointer flex flex-col items-center gap-2">
                    <span class="material-symbols-outlined text-4xl text-slate-400">upload_file</span>
                    <span class="font-bold text-slate-700 dark:text-white">Diplôme du Baccalauréat <span class="text-red-500">*</span></span>
                    <span class="text-xs text-slate-500" id="doc_bac_name">Cliquer pour parcourir</span>
                </label>
            </div>

            <div class="border-2 border-dashed border-slate-200 dark:border-slate-700 rounded-lg p-6 text-center hover:border-primary transition-colors bg-slate-50 dark:bg-slate-900/50">
                <input type="file" id="doc_id" name="doc_id" accept=".pdf,.jpg,.png" class="hidden">
                <label for="doc_id" class="cursor-pointer flex flex-col items-center gap-2">
                    <span class="material-symbols-outlined text-4xl text-slate-400">badge</span>
                    <span class="font-bold text-slate-700 dark:text-white">Pièce d'identité <span class="text-red-500">*</span></span>
                    <span class="text-xs text-slate-500" id="doc_id_name">Cliquer pour parcourir</span>
                </label>
            </div>
            
            <!-- Hide actual file required validation for demo smoothness, rely on js validation -->
        </div>
        </div>
    </div>

    <!-- Step 4: Récapitulatif -->
    <div class="form-step hidden" data-step="4">
        <div class="bg-white dark:bg-[#1a2c2b] rounded-xl shadow-lg border border-slate-100 dark:border-slate-800 overflow-hidden">
        <div class="p-6 border-b border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-800/30 flex justify-between items-center">
            <h3 class="text-lg font-bold text-secondary dark:text-white flex items-center gap-2">
                <span class="material-symbols-outlined text-primary">done_all</span> Récapitulatif
            </h3>
            <span class="text-xs bg-primary/10 text-primary px-2 py-1 rounded font-bold">Étape 4/4</span>
        </div>
        <div class="p-6 sm:p-8 flex flex-col gap-6">
            <div class="bg-slate-50 dark:bg-slate-800/50 p-4 rounded-lg flex flex-col gap-3 text-sm">
                <div class="flex flex-col sm:flex-row sm:justify-between border-b border-slate-200 dark:border-slate-700 pb-2">
                    <span class="text-slate-500">Nom complet</span>
                    <span class="font-bold text-slate-900 dark:text-white" id="summary-name">-</span>
                </div>
                <div class="flex flex-col sm:flex-row sm:justify-between border-b border-slate-200 dark:border-slate-700 pb-2">
                    <span class="text-slate-500">Email</span>
                    <span class="font-bold text-slate-900 dark:text-white" id="summary-email">-</span>
                </div>
                <div class="flex flex-col sm:flex-row sm:justify-between border-b border-slate-200 dark:border-slate-700 pb-2">
                    <span class="text-slate-500">Filière</span>
                    <span class="font-bold text-slate-900 dark:text-white" id="summary-filiere">-</span>
                </div>
                <div class="flex flex-col sm:flex-row sm:justify-between pb-2">
                    <span class="text-slate-500">Documents</span>
                    <span class="font-bold text-green-600 dark:text-green-400 flex items-center gap-1"><span class="material-symbols-outlined text-[16px]">check_circle</span> Joints</span>
                </div>
            </div>
            
            <label class="flex items-start gap-3 mt-4 cursor-pointer">
                <input type="checkbox" required class="mt-1 rounded border-slate-300 text-primary focus:ring-primary shadow-sm" name="terms">
                <span class="text-sm text-slate-600 dark:text-slate-300">
                    Je certifie que les informations fournies sont exactes et j'accepte les conditions d'admission de l'USIH.
                </span>
            </label>
        </div>
        </div>
    </div>

    <!-- Navigation Buttons -->
    <div class="flex items-center justify-between pt-4">
        <button id="btn-prev" class="px-6 h-12 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-500 font-bold hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors disabled:opacity-50" disabled type="button">
            <span class="hidden sm:inline">Précédent</span>
            <span class="material-symbols-outlined sm:hidden">arrow_back</span>
        </button>
        <button id="btn-next" class="group relative overflow-hidden px-8 h-12 rounded-lg bg-primary text-white font-bold hover:bg-primary-dark transition-all shadow-[0_4px_14px_0_rgba(184,46,59,0.39)] hover:shadow-[0_6px_20px_rgba(184,46,59,0.23)] hover:-translate-y-1 active:translate-y-0" type="button">
            <div class="absolute inset-0 w-3 border-r-2 border-white/20 skew-x-[-25deg] group-hover:animate-[shine_1s_infinite]"></div>
            <span class="flex items-center gap-2">
                Suivant
                <span class="material-symbols-outlined">arrow_forward</span>
            </span>
        </button>
        <button id="btn-submit" class="hidden group relative overflow-hidden px-8 h-12 rounded-lg bg-green-600 text-white font-bold hover:bg-green-700 transition-all shadow-lg hover:-translate-y-1 active:translate-y-0" type="submit">
            <div class="absolute inset-0 w-full bg-white/20 scale-x-0 origin-left group-hover:scale-x-100 transition-transform"></div>
            <span class="flex items-center gap-2 relative z-10">
                Soumettre ma demande
                <span class="material-symbols-outlined">send</span>
            </span>
        </button>
    </div>
</form>
</div>
<!-- Right Column: Info & Sticky Sidebar -->
<div class="lg:col-span-4 flex flex-col gap-6">
<!-- Fees Card -->
<div class="bg-gradient-to-br from-primary to-primary-dark rounded-xl shadow-lg p-6 text-white relative overflow-hidden group">
<div class="absolute -right-10 -top-10 w-32 h-32 bg-white/10 rounded-full blur-2xl group-hover:bg-white/20 transition-all duration-700"></div>
<div class="absolute -left-10 -bottom-10 w-32 h-32 bg-black/5 rounded-full blur-2xl"></div>
<div class="relative z-10 flex flex-col gap-1">
<div class="flex items-start justify-between">
<span class="material-symbols-outlined text-4xl mb-4 bg-white/20 p-2 rounded-lg backdrop-blur-sm">payments</span>
<span class="text-xs font-bold uppercase tracking-wider bg-white/20 px-2 py-1 rounded backdrop-blur-sm">Obligatoire</span>
</div>
<h3 class="text-lg font-medium opacity-90">Frais de dossier</h3>
<p class="text-3xl font-black tracking-tight mb-2">100 000 FCFA</p>
<p class="text-sm opacity-80 leading-relaxed border-t border-white/20 pt-3 mt-1">
                            Montant non remboursable à régler lors de la validation finale du dossier.
                        </p>
</div>
</div>
<!-- Support Card -->
<div class="bg-white dark:bg-[#1a2c2b] rounded-xl shadow-sm border border-slate-100 dark:border-slate-800 p-6 flex flex-col gap-4">
<h4 class="font-bold text-secondary dark:text-white flex items-center gap-2">
<span class="material-symbols-outlined text-primary">support_agent</span>
                        Besoin d'aide ?
                    </h4>
<p class="text-sm text-slate-500 dark:text-slate-400">
                        Notre équipe d'admission est disponible pour vous assister dans votre démarche.
                    </p>
<div class="flex flex-col gap-3">
<a class="flex items-center gap-3 text-sm font-medium text-slate-700 dark:text-slate-300 hover:text-primary transition-colors p-3 rounded-lg bg-slate-50 dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700" href="#">
<span class="material-symbols-outlined text-primary">call</span>
                            +241 01 02 03 04
                        </a>
<a class="flex items-center gap-3 text-sm font-medium text-slate-700 dark:text-slate-300 hover:text-primary transition-colors p-3 rounded-lg bg-slate-50 dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700" href="mailto:jmoussouami@icloud.com">
<span class="material-symbols-outlined text-primary">mail</span>
                            jmoussouami@icloud.com
                        </a>
</div>
</div>
<!-- Doc Checklist (Preview of what's needed) -->
<div class="bg-white dark:bg-[#1a2c2b] rounded-xl shadow-sm border border-slate-100 dark:border-slate-800 p-6">
<h4 class="font-bold text-secondary dark:text-white mb-4 text-sm uppercase tracking-wide text-slate-400">Documents Requis</h4>
<ul class="space-y-3">
<li class="flex items-start gap-3 text-sm text-slate-600 dark:text-slate-300 border-b border-slate-100 dark:border-slate-800 pb-2">
<span class="material-symbols-outlined text-primary text-[20px] shrink-0">check_circle</span>
<span>Relevés de notes (Bac / Licence)</span>
</li>
<li class="flex items-start gap-3 text-sm text-slate-600 dark:text-slate-300 border-b border-slate-100 dark:border-slate-800 pb-2">
<span class="material-symbols-outlined text-primary text-[20px] shrink-0">check_circle</span>
<span>Copie légalisée du diplôme</span>
</li>
<li class="flex items-start gap-3 text-sm text-slate-600 dark:text-slate-300">
<span class="material-symbols-outlined text-primary text-[20px] shrink-0">check_circle</span>
<span>Pièce d'identité valide</span>
</li>
</ul>
</div>
</div>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const steps = document.querySelectorAll('.form-step');
    const stepperGroups = document.querySelectorAll('#stepper .group');
    const stepLines = [
        document.getElementById('line-1'),
        document.getElementById('line-2'),
        document.getElementById('line-3')
    ];
    
    const btnNext = document.getElementById('btn-next');
    const btnPrev = document.getElementById('btn-prev');
    const btnSubmit = document.getElementById('btn-submit');
    const form = document.getElementById('multi-step-form');
    
    let currentStep = 1;
    const totalSteps = 4;

    // File inputs text update
    document.getElementById('doc_bac').addEventListener('change', function(e) {
        if(e.target.files.length) document.getElementById('doc_bac_name').textContent = e.target.files[0].name;
    });
    document.getElementById('doc_id').addEventListener('change', function(e) {
        if(e.target.files.length) document.getElementById('doc_id_name').textContent = e.target.files[0].name;
    });

    function updateUI() {
        // Show/hide steps
        steps.forEach(s => {
            if(parseInt(s.dataset.step) === currentStep) {
                s.classList.remove('hidden');
            } else {
                s.classList.add('hidden');
            }
        });

        // Update stepper visuals
        stepperGroups.forEach(g => {
            const s = parseInt(g.dataset.step);
            const circle = g.querySelector('.step-circle');
            if (s < currentStep) {
                g.classList.remove('opacity-60');
                circle.classList.add('bg-primary', 'text-white');
                circle.classList.remove('bg-slate-100', 'border-2');
                circle.innerHTML = '<span class="material-symbols-outlined text-sm">check</span>';
            } else if (s === currentStep) {
                g.classList.remove('opacity-60');
                circle.classList.add('bg-primary', 'text-white', 'shadow-[0_0_0_4px_rgba(184,46,59,0.2)]');
                circle.classList.remove('bg-slate-100', 'border-2');
                circle.innerHTML = s;
            } else {
                g.classList.add('opacity-60');
                circle.classList.remove('bg-primary', 'text-white', 'shadow-[0_0_0_4px_rgba(184,46,59,0.2)]');
                circle.classList.add('bg-slate-100', 'border-2', 'dark:bg-slate-800');
                circle.innerHTML = s;
            }
        });

        // Update lines
        stepLines.forEach((line, index) => {
            if (index < currentStep - 1) {
                line.style.width = '100%';
            } else if (index === currentStep - 1) {
                line.style.width = '50%';
            } else {
                line.style.width = '0%';
            }
        });

        // Buttons
        btnPrev.disabled = currentStep === 1;
        
        if (currentStep === totalSteps) {
            btnNext.classList.add('hidden');
            btnSubmit.classList.remove('hidden');
            
            // Populate summary
            document.getElementById('summary-name').textContent = document.getElementById('firstname').value + ' ' + document.getElementById('lastname').value;
            document.getElementById('summary-email').textContent = document.getElementById('email').value;
            document.getElementById('summary-filiere').textContent = document.getElementById('filiere').value || 'Non spécifié';
            
            // Show web3forms notice if access key is still default
            if(document.querySelector('input[name="access_key"]').value === "YOUR_ACCESS_KEY_HERE") {
                document.getElementById('web3forms-notice').classList.remove('hidden');
            }
        } else {
            btnNext.classList.remove('hidden');
            btnSubmit.classList.add('hidden');
            document.getElementById('web3forms-notice').classList.add('hidden');
        }
    }

    function validateStep(stepIndex) {
        const step = document.querySelector(`.form-step[data-step="${stepIndex}"]`);
        const inputs = step.querySelectorAll('input[required], select[required]');
        let isValid = true;
        
        // Simple HTML5 validity check
        inputs.forEach(input => {
            if (!input.checkValidity()) {
                input.classList.add('border-red-500', 'ring-red-500');
                isValid = false;
            } else {
                input.classList.remove('border-red-500', 'ring-red-500');
            }
        });

        // Special case for step 3: Check files manually
        if (stepIndex === 3) {
            const f1 = document.getElementById('doc_bac');
            const f2 = document.getElementById('doc_id');
            if(!f1.files.length) {
                f1.parentNode.classList.add('border-red-500');
                isValid = false;
            } else {
                f1.parentNode.classList.remove('border-red-500');
            }
            if(!f2.files.length) {
                f2.parentNode.classList.add('border-red-500');
                isValid = false;
            } else {
                f2.parentNode.classList.remove('border-red-500');
            }
        }

        if(!isValid) {
            alert("Veuillez remplir tous les champs obligatoires correctement avant de continuer.");
        }
        return isValid;
    }

    btnNext.addEventListener('click', () => {
        if (validateStep(currentStep)) {
            currentStep++;
            window.scrollTo({ top: document.querySelector('.bg-white.dark\\:bg-\\[\\#1a2c2b\\]').offsetTop - 100, behavior: 'smooth' });
            updateUI();
        }
    });

    btnPrev.addEventListener('click', () => {
        currentStep--;
        window.scrollTo({ top: document.querySelector('.bg-white.dark\\:bg-\\[\\#1a2c2b\\]').offsetTop - 100, behavior: 'smooth' });
        updateUI();
    });

    // Handle manual form submit event (prevent default if access key is missing for demo, or let standard HTML submit handle it)
    form.addEventListener('submit', (e) => {
        if (!validateStep(4)) {
            e.preventDefault();
            return;
        }
        const ak = document.querySelector('input[name="access_key"]').value;
        if(ak === "YOUR_ACCESS_KEY_HERE") {
            e.preventDefault();
            alert("En mode de production, ce formulaire sera envoyé à jmoussouami@icloud.com. N'oubliez pas d'ajouter votre clé Web3Forms !");
            // If they just want mailto fallback:
            const body = encodeURIComponent(`Nouvelle pré-inscription:\nNom: ${document.getElementById('lastname').value}\nPrénom: ${document.getElementById('firstname').value}\nEmail: ${document.getElementById('email').value}\nFilière: ${document.getElementById('filiere').value}`);
            window.location.href = `mailto:jmoussouami@icloud.com?subject=Nouvelle Pré-inscription USIH&body=${body}`;
        }
    });

    // Initialize UI
    updateUI();
});
</script>
</main>"""

# Replace in content using regex to find the main tag boundaries.
# main starts with <main... and ends with </main>
import re
new_content = re.sub(r'<main.*?</main>', main_replacement, content, flags=re.DOTALL)

with open(f_name, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated pre-inscription.html successfully.")
