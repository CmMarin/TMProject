# Chronicles of the Shattered Veil
# Prequel: Introduction

# Define Characters
define e = Character("Elara Voss", color="#c8a2c8")
define t = Character("Thorne Blackwood", color="#4e6b8a")
define s = Character("Director Seraphina Krel", color="#b22222")
define z = Character("Zephyr", color="#7fffd4")
define m = Character("Maven", color="#20b2aa")
define l = Character("Dr. Lena Rey", color="#8a2be2")

# Define Flags to Track Choices
default asked_about_elara = False
default asked_about_maven = False
default asked_about_veil = False
default asked_about_thorne_role = False
default asked_about_umbral_covenant = False
default asked_about_thorne_motivations = False
default asked_about_nexus_corp = False
default asked_about_krel_goals = False
default asked_about_krel_past = False
default asked_about_zephyr_origins = False
default asked_about_veil_instability = False
default asked_about_elara_role = False

# New Flags for Ending Tracking
default trust_thorne = False
default resist_nexus = False
default stabilize_veil = False
default confront_krel = False

# Start the game by jumping to the prologue
label start:
    jump prologue

# Prologue: The World of 3016
label prologue:
    "The year is 3016. The world is divided between towering metropolises of advanced technology and wildlands where magic has resurged."
    "For centuries, humanity has manipulated dimensional energy, but now the boundaries between reality and the ethereal realm are weakening."
    "In this fractured world, one woman holds the key to restoring balance—or destroying it forever."

    # Introduction to Elara
    e "Another day, another report. Maven, compile the data from yesterday's experiments and send it to Dr. Rey."
    m "Data compiled and sent. You've been working late again, Elara. Your neural fatigue levels are rising."
    e "I know, but this research is important. If we can harness dimensional energy safely, it could change everything."
    m "Understood. But remember: even the brightest minds need rest."
    e "I'll rest when this is done."

    # Dialogue Choices to Learn About Elara
    label menu_label_elara:
        menu:
            "Ask about Elara's background" if not asked_about_elara:
                e "I've always been fascinated by the unknown. That's why I joined Nexus Corporation's Dimensional Research Division."
                e "But after years of working there, I realized they weren't interested in understanding the veil—they wanted to control it."
                e "That's why I left. I couldn't be part of something so... exploitative."
                $ asked_about_elara = True
                jump menu_label_elara

            "Ask about Maven" if not asked_about_maven:
                e "Maven's my AI assistant. She's integrated into my neural implant, so she's always with me."
                m "I am programmed to assist you in all tasks, Elara. Though I must admit, your tendency to overwork complicates my protocols."
                e "She's more than just a program, though. She's my partner in all this."
                $ asked_about_maven = True
                jump menu_label_elara

            "Ask about the veil" if not asked_about_veil:
                e "The veil is the boundary between our world and the ethereal realm. It's been weakening for years, and no one knows why."
                e "Some say it's because of humanity's experiments with dimensional energy. Others think it's a natural phenomenon."
                e "All I know is that if it collapses, the consequences will be catastrophic."
                $ asked_about_veil = True
                jump menu_label_elara

        # Check if all Elara choices have been made
        if asked_about_elara and asked_about_maven and asked_about_veil:
            jump introduction_to_thorne

    # Introduction to Thorne
    label introduction_to_thorne:
        "Meanwhile, in the wildlands..."
        t "The veil grows weaker every day. If we don't act soon, it will tear completely."
        "Thorne Blackwood, a member of the secretive Umbral Covenant, patrols the wildlands, watching for signs of veil instability."
        "His mission: protect the natural order of dimensions at all costs."

        # Dialogue Choices to Learn About Thorne
        label menu_label_thorne:
            menu:
                "Ask about Thorne's role" if not asked_about_thorne_role:
                    t "I'm a guardian of the veil. The Umbral Covenant has protected the boundaries between worlds for centuries."
                    t "We're not just fighting to preserve our world—we're fighting to preserve all worlds."
                    $ asked_about_thorne_role = True
                    jump menu_label_thorne

                "Ask about the Umbral Covenant" if not asked_about_umbral_covenant:
                    t "The Covenant is a group of individuals who can perceive the veil. We've dedicated our lives to maintaining the balance."
                    t "But we're not the only ones who know about the veil. Nexus Corporation is trying to exploit it for their own gain."
                    $ asked_about_umbral_covenant = True
                    jump menu_label_thorne

                "Ask about Thorne's motivations" if not asked_about_thorne_motivations:
                    t "I've seen what happens when the veil weakens. Entire dimensions collapse, taking countless lives with them."
                    t "I won't let that happen again. Not on my watch."
                    $ asked_about_thorne_motivations = True
                    jump menu_label_thorne

            # Check if all Thorne choices have been made
            if asked_about_thorne_role and asked_about_umbral_covenant and asked_about_thorne_motivations:
                jump introduction_to_krel

    # Introduction to Director Krel
    label introduction_to_krel:
        s "The veil is the key to humanity's future. And we will control it."
        "Director Seraphina Krel, head of Nexus Corporation's Dimensional Research Division, oversees the company's efforts to harness veil energy."
        "Her methods are ruthless, but her vision is clear: power at any cost."

        # Dialogue Choices to Learn About Director Krel
        label menu_label_krel:
            menu:
                "Ask about Nexus Corporation" if not asked_about_nexus_corp:
                    s "Nexus is the pinnacle of human achievement. We've pushed the boundaries of science and technology further than anyone thought possible."
                    s "But the veil is our greatest challenge—and our greatest opportunity."
                    $ asked_about_nexus_corp = True
                    jump menu_label_krel

                "Ask about her goals" if not asked_about_krel_goals:
                    s "I want to secure humanity's future. If that means bending the veil to our will, so be it."
                    s "The ends justify the means, Elara. You of all people should understand that."
                    $ asked_about_krel_goals = True
                    jump menu_label_krel

                "Ask about her past with Elara" if not asked_about_krel_past:
                    s "Elara was one of our brightest researchers. But she left when she realized what we were truly capable of."
                    s "A shame, really. She could have been a valuable asset."
                    $ asked_about_krel_past = True
                    jump menu_label_krel

            # Check if all Krel choices have been made
            if asked_about_nexus_corp and asked_about_krel_goals and asked_about_krel_past:
                jump introduction_to_zephyr

    # Introduction to Zephyr
    label introduction_to_zephyr:
        z "Elara... You are the bridge. The one who can mend the shattered veil."
        "Zephyr, an enigmatic entity from beyond the veil, communicates with those who can perceive its presence."
        "Its motives are unclear, but its warnings are dire."

        # Dialogue Choices to Learn About Zephyr
        label menu_label_zephyr:
            menu:
                "Ask about Zephyr's origins" if not asked_about_zephyr_origins:
                    z "I am a fragment of the veil itself. A voice from the beyond, guiding those who can hear."
                    z "But my purpose is not to explain—it is to warn."
                    $ asked_about_zephyr_origins = True
                    jump menu_label_zephyr

                "Ask about the veil's instability" if not asked_about_veil_instability:
                    z "The veil weakens because of humanity's hubris. Your experiments have torn its fabric."
                    z "If it collapses, all dimensions will be consumed by chaos."
                    $ asked_about_veil_instability = True
                    jump menu_label_zephyr

                "Ask about Elara's role" if not asked_about_elara_role:
                    z "Elara is unique. She is the bridge between worlds, the one who can restore balance."
                    z "But the choice is hers. Will she mend the veil—or destroy it?"
                    $ asked_about_elara_role = True
                    jump menu_label_zephyr

            # Check if all Zephyr choices have been made
            if asked_about_zephyr_origins and asked_about_veil_instability and asked_about_elara_role:
                jump start_main_story

    # Transition to Main Story
    label start_main_story:
        "As the veil grows weaker, the paths of these individuals will converge."
        "Elara Voss, Thorne Blackwood, Director Krel, and Zephyr are all players in a game that will determine the fate of worlds."
        "The question is: what role will you play?"

        jump act_i

# Act I: The Awakening
label act_i:
    e "I can't believe what I just saw... Was that real? Or am I losing my mind?"
    m "Elara, your neural patterns are showing unusual activity. Should I run a diagnostic?"
    e "No, Maven. This isn't a glitch. It's something... else."
    m "If you insist. But I recommend caution. Unusual neural activity could indicate a malfunction."
    e "It's not a malfunction. I saw... a tear in reality. Like a shimmering curtain, and beyond it... something I can't explain."
    m "Interesting. Would you like me to record this observation for future analysis?"
    e "Not yet. I need to figure this out on my own first."

    # First Veil Vision
    z "\[echoing voice\] Elara... You are the bridge. The one who can mend the shattered veil."
    e "Who's there? Who's speaking?"
    z "I am Zephyr. A guide... a voice from beyond. You are needed, Elara."
    e "Needed for what? What's happening to me?"
    z "The veil weakens. You must choose: embrace your gift or turn away."

    # Choice: How does Elara respond to her first vision?
    menu:
        "Investigate privately":
            e "I need to understand this on my own. Maven, keep this quiet. No records, no traces."
            m "Understood. Privacy mode activated."
            jump investigate_privately

        "Consult with former Nexus colleagues":
            e "Maybe someone at Nexus knows what's happening. I'll reach out to Dr. Lena Rey."
            m "Establishing connection to Dr. Rey. Be cautious, Elara. Nexus may not have your best interests at heart."
            jump consult_nexus

        "Ignore and suppress abilities":
            e "This is too much. I need to focus on reality, not... whatever this is."
            m "Suppressing neural activity. Warning: prolonged suppression may lead to instability."
            jump ignore_abilities

# Branch 1: Investigate Privately
label investigate_privately:
    e "If I'm going to figure this out, I need to start with what I know. Maven, pull up all records on dimensional energy research."
    m "Accessing archives. Be advised: some files are classified and may require bypassing security protocols."
    e "Do it. I need answers."
    t "\[approaching cautiously\] The veil shimmers around you. You can see them, can't you?"
    e "Who are you? And how do you know what I'm seeing?"
    t "I'm Thorne Blackwood, from the Umbral Covenant. We protect the boundaries between worlds. And you, Elara, are one of the few who can see the veils."
    e "The Umbral Covenant? I've heard rumors, but I thought you were just a myth."
    t "We're very real. And so is the danger you're in. Nexus Corporation is already tracking you."
    e "What do you want from me?"
    t "To help you. But the choice is yours. Will you trust me?"
    menu:
        "Trust Thorne":
            e "Alright, Thorne. I'll trust you. For now."
            t "Good. Follow me. We have much to discuss."
            $ trust_thorne = True
            jump act_ii
        "Refuse":
            e "I don't know you. I'll figure this out on my own."
            t "Suit yourself. But don't say I didn't warn you."
            jump act_ii

# Branch 2: Consult with Nexus
label consult_nexus:
    e "Dr. Rey, it's Elara. I need your help with something... unusual."
    l "Elara! It's been a while. What's going on?"
    e "I've been experiencing... visions. Like I can see into another dimension. Do you know anything about this?"
    l "Visions? That's fascinating. It sounds like you've developed a connection to the veil. Nexus has been researching this for years."
    e "What do you mean? What's the veil?"
    l "It's a dimensional boundary, Elara. And if you can see it, you're incredibly special. Come to the lab. We'll run some tests."
    e "Alright. I'll be there."
    s "Elara Voss. I've been expecting you."
    e "Director Krel? What are you doing here?"
    s "Dr. Rey informed me of your... condition. We're very interested in your abilities."
    e "I didn't agree to this."
    s "You don't have to. Nexus owns all research conducted by its employees, past or present. You're coming with us."
    menu:
        "Resist":
            e "I won't let you use me!"
            s "You don't have a choice."
            $ resist_nexus = True
            jump act_ii
        "Comply":
            e "Fine. But don't think I'll cooperate willingly."
            s "We'll see about that."
            jump act_ii

# Branch 3: Ignore Abilities
label ignore_abilities:
    e "This is too much. I need to focus on my work, not these... hallucinations."
    m "Suppression protocols active. Warning: neural activity is spiking. Prolonged suppression may lead to instability."
    e "I don't care. Just make it stop!"
    z "\[echoing voice]\ You cannot ignore your destiny, Elara."
    e "Leave me alone! I don't want this!"
    z "The veil will not wait. The choice is yours."
    e "I can't keep this hidden anymore. I need help."
    menu:
        "Reach out to Thorne":
            e "Maven, find me Thorne Blackwood. I need to talk to him."
            m "Contacting Thorne Blackwood. Be cautious, Elara."
            $ trust_thorne = True
            jump act_ii
        "Return to Nexus":
            e "Maven, contact Dr. Rey. Tell her I'm ready to talk."
            m "Establishing connection. Be advised: Nexus may not have your best interests at heart."
            jump act_ii

# Act II: The Journey
label act_ii:
    e "The more I learn about the veil, the more questions I have. What is it? Why can I see it?"
    t "The veil is a living entity, Elara. It exists between dimensions, and it chooses who can see it. You were chosen for a reason."
    e "A reason? What reason?"
    t "That's what we need to find out. But beware—Nexus Corporation is already hunting you."
    z "\[echoing voice\] Elara... You are the bridge. The one who can mend the shattered veil."
    e "Who's there? Who's speaking?"
    t "It's Zephyr. An entity from beyond the veil. It's been trying to communicate with you."
    e "What does it want from me?"
    z "Balance... Restoration... You hold the key."

    # Complications: Betrayal
    s "Elara Voss. We've been looking for you."
    e "Director Krel? What are you doing here?"
    s "You have something we need. Your abilities could change everything. Join us, and we can harness the veil's power together."
    e "I won't let you exploit the veil for your own gain. It's too dangerous."
    s "You don't have a choice, Elara. You're coming with us, one way or another."

    # Choice: How does Elara respond to Krel's ultimatum?
    menu:
        "Fight back with Thorne":
            e "Thorne, we can't let them take me. We have to fight!"
            t "Agreed. Stay close to me, and we'll get out of this together."
            jump fight_back_with_thorne

        "Surrender to Krel":
            e "Fine. I'll go with you. But this isn't over."
            s "Good choice, Elara. You'll see the bigger picture soon enough."
            jump surrender_to_krel

        "Use the veil's power":
            e "I don't know how, but I have to try. Zephyr, if you can hear me, help me!"
            z "\[echoing voice\] Embrace the veil, Elara. Let it flow through you."
            $ stabilize_veil = True
            jump use_veil_power

# Branch 1: Fight Back with Thorne
label fight_back_with_thorne:
    t "We need to get to the Umbral Covenant's stronghold. It's the only place where you'll be safe from Nexus."
    e "But what about the veil? If it's weakening, we can't just hide."
    t "We're not hiding. We're regrouping. The Covenant has resources that can help us stabilize the veil—and protect you."
    e "Alright. Lead the way."
    "Thorne and Elara make their way to the Umbral Covenant's stronghold, a hidden sanctuary deep in the wildlands."
    t "This is where we'll plan our next move. Nexus won't find us here."
    e "What's the plan, Thorne? How do we stop them?"
    t "First, we need to strengthen your connection to the veil. The stronger your bond, the more control you'll have over its energy."
    e "And then?"
    t "Then we strike back. Nexus won't stop until they control the veil. We have to stop them before it's too late."
    $ stabilize_veil = True
    jump act_iii

# Branch 2: Surrender to Krel
label surrender_to_krel:
    s "Welcome back, Elara. I knew you'd see reason."
    e "I'm not here because I want to be. I'm here because I don't have a choice."
    s "You always have a choice. And soon, you'll understand why this is the right one."
    e "What do you mean?"
    s "The veil is a source of infinite power. With your abilities, we can harness it and secure humanity's future."
    e "At what cost? You're playing with forces you don't understand."
    s "We understand more than you think. And with your help, we'll understand even more."
    menu:
        "Cooperate with Krel":
            e "Fine. I'll help you. But if this goes wrong, it's on you."
            s "That's the spirit. Let's get to work."
            jump cooperate_with_krel

        "Sabotage Nexus from within":
            e "Alright, Director Krel. I'll do what you ask. But I'm not doing it for you."
            s "As long as you cooperate, I don't care why you're doing it."
            $ confront_krel = True
            jump sabotage_nexus

# Branch 3: Use the Veil's Power
label use_veil_power:
    e "Zephyr, I need your help. Show me how to use this power."
    z "\[echoing voice\] Focus, Elara. Let the veil flow through you. Feel its energy."
    e "I... I can feel it. It's like nothing I've ever experienced before."
    z "Now, direct it. Use it to protect yourself."
    e "Director Krel, you're not taking me anywhere."
    s "What are you—?"
    e "I won't let you control me. Or the veil."
    "Elara channels the veil's energy, creating a barrier that repels Krel and her forces."
    s "This isn't over, Elara. You can't run forever."
    e "I'm not running. I'm fighting back."
    jump act_iii

# New labels to implement missing branches
label cooperate_with_krel:
    "Elara begins working with Nexus, helping them understand the veil better."
    e "If I'm going to do this, we need to be careful. The veil is fragile."
    s "Of course, Elara. We value your expertise."
    "As time passes, Elara begins to see Director Krel's vision more clearly."
    e "Maybe there is a way to harness the veil's energy safely. To benefit humanity."
    s "I knew you'd understand eventually. Together, we'll make history."
    $ stabilize_veil = False
    $ confront_krel = False
    jump act_iii

label sabotage_nexus:
    "Elara pretends to cooperate with Nexus, while secretly looking for ways to undermine their plans."
    e "I'll need full access to your research facilities and data. To help properly, of course."
    s "Granted. Just remember, we're watching you, Elara."
    "When no one is looking, Elara begins to sabotage Nexus's experiments."
    e "If I can corrupt their data subtly enough, they'll never achieve their goals without realizing why."
    m "Be careful, Elara. If they catch you, the consequences will be severe."
    e "I know. But I have to try."
    $ stabilize_veil = False
    jump act_iii

# Act III: The Convergence
label act_iii:
    z "\[echoing voice\] The veil grows weaker, Elara. Time is running out."
    e "I know. But I'm not ready. I don't know how to fix this."
    z "You are the bridge. The veil responds to your will. Trust yourself."
    e "What if I fail?"
    z "Then all will be lost. But you must try."

    # Final Choice: How does Elara approach the final confrontation?
    menu:
        "Confront Krel directly":
            e "I'm done running. It's time to face Krel and end this."
            $ confront_krel = True
            jump confront_krel_directly

        "Seek Thorne's guidance":
            e "I need Thorne's help. Together, we can stabilize the veil."
            $ stabilize_veil = True
            jump seek_thorne_guidance

        "Embrace the veil's power fully":
            e "If I'm the bridge, then I need to fully embrace the veil's power. No more holding back."
            $ stabilize_veil = True
            jump embrace_veil_power

# Branch 1: Confront Krel Directly
label confront_krel_directly:
    e "Director Krel, this ends now."
    s "Elara. I was wondering when you'd show up. Ready to join us?"
    e "No. I'm here to stop you."
    s "You can't stop progress, Elara. The veil's power belongs to humanity."
    e "Not if it destroys us first."
    "Elara and Krel face off in a final confrontation, with the fate of the veil hanging in the balance."
    jump final_showdown

# Branch 2: Seek Thorne's Guidance
label seek_thorne_guidance:
    e "Thorne, I need your help. The veil is on the brink of collapse."
    t "I know. But together, we can stabilize it. The Covenant has a ritual that can strengthen the veil, but it requires your connection to it."
    e "What do I need to do?"
    t "You'll need to channel the veil's energy through yourself. It's dangerous, but it's the only way."
    e "Then let's do it. I'm ready."
    jump final_ritual

# Branch 3: Embrace the Veil's Power Fully
label embrace_veil_power:
    e "Zephyr, I'm ready. Show me how to fully embrace the veil."
    z "\[echoing voice\] Let go of your fears, Elara. Become one with the veil."
    e "I... I can feel it. It's like I'm part of something much larger."
    z "You are. Now, use that power to restore balance."
    jump final_convergence

# Final Showdown
label final_showdown:
    "Elara and Krel clash in a battle of wills, with the veil's energy swirling around them."
    e "You can't control this, Krel. It's too powerful."
    s "I don't need to control it. I just need to use it."
    "In the end, Elara's connection to the veil proves stronger, and Krel is forced to retreat."
    e "It's over. The veil is safe—for now."

    # Check which ending to trigger based on previous choices
    if trust_thorne and resist_nexus:
        jump ending_resistance
    elif not trust_thorne and not resist_nexus and not confront_krel:
        jump ending_reformer
    elif stabilize_veil and confront_krel:
        jump ending_transcendence
    elif not trust_thorne and not stabilize_veil and confront_krel:
        jump ending_saboteur
    else:
        jump ending

# Final Ritual
label final_ritual:
    "Elara and Thorne perform the ritual, channeling the veil's energy to stabilize it."
    t "You're doing it, Elara. Just a little more."
    e "I can feel it... the veil is responding."
    "The ritual succeeds, and the veil is restored to its former strength."
    e "We did it. The veil is stable again."

    # Check which ending to trigger based on previous choices
    if trust_thorne and stabilize_veil and not confront_krel:
        jump ending_balance
    elif trust_thorne and resist_nexus:
        jump ending_resistance
    else:
        jump ending

# Final Convergence
label final_convergence:
    "Elara fully embraces the veil's power, becoming one with it."
    e "I understand now. The veil isn't just a boundary—it's a living entity."
    z "\[echoing voice\] You have restored balance, Elara. The veil thanks you."
    "With her newfound connection, Elara stabilizes the veil and ensures the safety of both worlds."

    # Check which ending to trigger based on previous choices
    if stabilize_veil and confront_krel:
        jump ending_transcendence
    elif trust_thorne and stabilize_veil:
        jump ending_balance
    elif not trust_thorne and not stabilize_veil and confront_krel:
        jump ending_saboteur
    else:
        jump ending

# Modified ending_balance to ensure it has a proper conclusion
label ending_balance:
    # Balanced ending that takes multiple factors into account
    "With the help of Thorne and the Umbral Covenant, Elara finds a path that preserves both worlds."
    e "The veil doesn't need to be controlled or destroyed - it needs to be understood."
    t "Together, we've found the balance that the veil requires."
    "Elara and Thorne establish a new order dedicated to maintaining harmony between dimensions."
    "Their work ensures that neither Nexus nor any other force can disrupt the delicate balance of the veil."
    "As guardians of the veil, they continue to protect the boundaries between worlds, knowing that balance requires eternal vigilance."
    "END: PERFECT BALANCE"
    return

# Ending based on Act I and Act II choices
label ending_resistance:
    # This ending occurs if the player trusted Thorne and resisted Nexus
    "With Thorne's guidance and Elara's determination to resist Nexus Corporation, they form a powerful alliance."
    e "We've stabilized the veil for now, but Nexus won't stop coming after us."
    t "The Umbral Covenant will protect you. Together, we'll form a new force to guard the veil."
    "Elara becomes a respected leader within the Covenant, using her unique connection to the veil to train others."
    e "I never imagined this would be my path, but it feels right."
    t "Sometimes the veil chooses our destiny for us."
    "The veil remains stable, and Elara and Thorne continue their vigil, watching for any signs of instability."
    "But Director Krel remains in the shadows, plotting her return..."
    "END: GUARDIAN OF THE COVENANT"
    return

# Ending if player collaborated with Nexus but tried to change it from within
label ending_reformer:
    # This happens if player didn't trust Thorne but tried to reform Nexus from within
    "Working within Nexus, Elara gradually influences their approach to the veil."
    e "If we respect the veil as a living entity rather than a resource to exploit, we can still harness its energy safely."
    s "Your results are impressive, Elara. Perhaps there is merit to your approach."
    "Over time, Elara transforms Nexus's Dimensional Research Division into an ethical organization."
    e "We've found balance between progress and preservation."
    m "Your neural patterns show contentment, Elara. This outcome has a 78% stability rating."
    "The veil stabilizes as Nexus's experiments become less invasive, creating a new era of responsible dimensional research."
    "But somewhere beyond the veil, Zephyr watches, knowing that balance is always temporary..."
    "END: THE REFORMER"
    return

# Ending for those who embrace the veil's power and confront Krel
label ending_transcendence:
    # This ending occurs if the player fully embraced the veil's power and confronted Krel
    "As Elara embraces the full power of the veil and confronts Director Krel, something unexpected happens."
    e "I can see everything now - all dimensions, all possibilities."
    s "What's happening to you, Elara?"
    "Elara's physical form begins to shimmer as she merges with the veil itself."
    e "I understand my purpose now. I don't just mend the veil - I am becoming part of it."
    z "You have transcended, Elara. You are now the Bridge incarnate."
    "Elara ascends beyond her human form, becoming a guardian entity that exists between dimensions."
    "From this state of transcendence, she can maintain balance across all realms, ensuring the veil remains strong."
    "Director Krel and Nexus are left humbled by the display of power they can never hope to control."
    "END: TRANSCENDENCE"
    return

# Ending for those who cooperate with Krel but ultimately betray Nexus
label ending_saboteur:
    # If player cooperated with Krel but intended to sabotage
    "After seemingly cooperating with Director Krel, Elara waits for the perfect moment to strike."
    e "You wanted to harness the veil's power, Director? Be careful what you wish for."
    "Elara activates a feedback loop in Nexus's dimensional technology, causing it to overload."
    s "What have you done?!"
    e "I've made sure no one can exploit the veil again. Not even Nexus."
    "The resulting cascade destroys years of Nexus research while simultaneously healing tears in the veil."
    "Elara escapes in the chaos, disappearing into the wildlands."
    "Years later, stories spread of a woman who walks between worlds, protecting the veil from those who would abuse it."
    "END: THE SABOTEUR"
    return

label ending:
    scene bg_city with fade
    "The veil is stable once more, and the threat of its collapse has been averted."
    "Elara’s journey has changed her forever, but she knows her work is far from over."
    e "The veil is safe—for now. But I’ll be ready if it ever needs me again."
    "And so, the Chronicles of the Shattered Veil continue..."
    return