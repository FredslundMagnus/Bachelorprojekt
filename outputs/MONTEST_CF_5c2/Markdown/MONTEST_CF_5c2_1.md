
# Parameters

    Name :                      MONTEST_CF_5c2-1
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Hours :                     22.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                5
    Counterfacts :              2
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      61698788109 function calls (61377653494 primitive calls) in 78909.30 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78909.301 78909.301 {built-in method builtins.exec}
                      1    4.896    4.896 78909.301 78909.301 <string>:1(<module>)
                      1  188.100  188.100 78904.405 78904.405 main.py:95(CFagent)
                2559018   12.848    0.000 19802.362    0.008 game.py:41(step)
                2559018   14.628    0.000 19296.662    0.008 layers.py:710(step)
                7677054   29.470    0.000 19213.312    0.003 agent.py:29(learn)
                2559018 2938.801    0.001 17081.138    0.007 agent.py:217(counterfact)
                7677054  487.347    0.000 15608.341    0.002 learner.py:42(Qlearn)
        356424061/35291137 1450.989    0.000 11794.039    0.000 module.py:866(_call_impl)
               27614083   78.468    0.000 11153.569    0.000 network.py:24(forward)
               27614083  352.261    0.000 10893.043    0.000 container.py:117(forward)
                2559019  416.554    0.000 10875.590    0.004 layers.py:676(update)
                2559018  232.941    0.000 8384.349    0.003 layers.py:17(step)
              237317889  742.797    0.000 8125.748    0.000 layer.py:98(move)
                2559018  278.989    0.000 7456.829    0.003 agent.py:54(_learn)
                2559018  277.496    0.000 6864.168    0.003 agent.py:209(_learn)
                4850512  101.852    0.000 6652.587    0.001 agent.py:172(choose_action)
                9968481  268.773    0.000 6489.159    0.001 agent.py:49(__call__)
                7677054   65.847    0.000 6089.756    0.001 optimizer.py:84(wrapper)
                7677054   35.138    0.000 5794.089    0.001 grad_mode.py:24(decorate_context)
                7677054  241.611    0.000 5684.524    0.001 adam.py:55(step)
                9869572   84.839    0.000 5674.201    0.001 layers.py:731(restart)
                2559018 3164.014    0.001 5551.069    0.002 replaybuffer.py:28(teleporter_save_data)
              237317889  538.302    0.000 5190.558    0.000 layers.py:727(check)
                7677054 1191.771    0.000 5173.064    0.001 _functional.py:53(adam)
               66380562 4914.707    0.000 4914.707    0.000 {built-in method tensor}
                2559018   81.022    0.000 4844.055    0.002 agent.py:117(_learn)
                9869572   42.615    0.000 4812.780    0.000 level.py:8(__init__)
               60415900   39.861    0.000 4786.957    0.000 game.py:37(board)
                9869572  777.936    0.000 4413.914    0.000 levels.py:418(generate)
                2559018 3189.441    0.001 4071.044    0.002 replaybuffer.py:22(sample_data)
               46062330 2660.478    0.000 4067.489    0.000 layer.py:151(update)
                7677054   31.025    0.000 4024.341    0.001 tensor.py:195(backward)
                7677054   31.010    0.000 3992.086    0.001 __init__.py:68(backward)
               55228166  130.756    0.000 3964.449    0.000 conv.py:398(forward)
                2559018 2288.784    0.001 3946.780    0.002 agent.py:88(interveen)
                7677054 3804.427    0.000 3804.427    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               55228166   79.826    0.000 3775.563    0.000 conv.py:390(_conv_forward)
                2559018 2927.690    0.001 3703.107    0.001 replaybuffer.py:49(sample_data)
               55228166 3695.737    0.000 3695.737    0.000 {built-in method conv2d}
              237317889 1906.289    0.000 3328.751    0.000 layers.py:531(check)
               77724213  167.898    0.000 3117.602    0.000 linear.py:93(forward)
               49347860  466.063    0.000 2892.984    0.000 level.py:41(notUsed)
               77724213   67.444    0.000 2869.882    0.000 functional.py:1737(linear)
               77724213 2785.927    0.000 2785.927    0.000 {built-in method torch._C._nn.linear}
              258381876 2514.229    0.000 2514.229    0.000 {built-in method clone}
                2559018 1408.369    0.001 2056.163    0.001 agent.py:67(modify)
              256346509  209.080    0.000 1798.931    0.000 {built-in method builtins.any}
              237224257  326.208    0.000 1688.782    0.000 layers.py:721(isFree)
              105338296   85.465    0.000 1653.325    0.000 activation.py:713(forward)
               12527499   81.499    0.000 1628.214    0.000 agent.py:59(modify_board)
             1737814728  517.755    0.000 1590.524    0.000 layers.py:692(<genexpr>)
             6173189130 1100.684    0.000 1579.691    0.000 enum.py:646(__hash__)
              105338296   90.669    0.000 1567.860    0.000 functional.py:1364(leaky_relu)
                2559018  802.715    0.000 1559.291    0.001 replaybuffer.py:55(CF_save_data)
               40676697 1499.019    0.000 1499.019    0.000 {built-in method cat}
              105338296 1459.024    0.000 1459.024    0.000 {built-in method torch._C._nn.leaky_relu}
             1393456671 1147.925    0.000 1362.574    0.000 layer.py:95(isFree)
                4850512 1075.346    0.000 1264.912    0.000 agent.py:183(convert_values)
               49347860   41.512    0.000 1259.695    0.000 level.py:38(elementsIn)
                2559018   45.337    0.000 1186.656    0.000 agent.py:168(__call__)
                2559018   41.953    0.000 1132.238    0.000 agent.py:112(__call__)
               12527499 1058.317    0.000 1058.317    0.000 {built-in method torch._C._nn.one_hot}
              143305008 1000.714    0.000 1000.714    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              251228472  611.683    0.000  973.350    0.000 layers.py:568(isDead)
              255901900  114.601    0.000  914.903    0.000 {built-in method builtins.all}
                7677054  161.375    0.000  895.837    0.000 optimizer.py:189(zero_grad)
              143305008  895.383    0.000  895.383    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2072552495  853.995    0.000  853.995    0.000 layer.py:146(elements)
             1084552136  317.084    0.000  834.314    0.000 layers.py:682(<genexpr>)
               54465896  324.600    0.000  833.728    0.000 random.py:315(sample)
              237317889  595.420    0.000  826.038    0.000 layers.py:71(check)
               49347860  406.429    0.000  805.086    0.000 level.py:39(<listcomp>)
             2105397207  802.605    0.000  802.605    0.000 level.py:32(inverse)
               59217432   76.583    0.000  755.140    0.000 layer.py:69(restart)
                2559018   49.280    0.000  687.434    0.000 replaybuffer.py:18(stacker)
              555430442  520.713    0.000  681.296    0.000 layer.py:126(remove)
                9968481  244.617    0.000  647.941    0.000 exploration.py:53(softmaxer)
              801115798  417.363    0.000  603.748    0.000 random.py:250(_randbelow_with_getrandbits)
              325039400  120.838    0.000  600.676    0.000 random.py:244(randint)
               71652504  597.404    0.000  597.404    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2559018   46.192    0.000  588.457    0.000 replaybuffer.py:45(stacker)
             1000740439  410.891    0.000  552.978    0.000 layer.py:130(add)
              273468393  548.473    0.000  548.473    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9869672  263.331    0.000  522.597    0.000 layers.py:30(reset)
               71652504  518.209    0.000  518.209    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              325039400  200.994    0.000  479.838    0.000 random.py:200(randrange)
             6173218393  479.012    0.000  479.012    0.000 {built-in method builtins.hash}
               71652504  476.544    0.000  476.544    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        5526589975/5526589972  412.519    0.000  475.787    0.000 {built-in method builtins.len}
               71652504  471.833    0.000  471.833    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             4782752907  462.566    0.000  462.566    0.000 layer.py:91(positions)
              255901900  304.979    0.000  450.900    0.000 layers.py:107(isDone)
               39589656  433.917    0.000  433.917    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              237317889  294.414    0.000  430.339    0.000 layers.py:42(check)
              501567612  336.583    0.000  418.543    0.000 tensor.py:906(grad)
               49347860  254.326    0.000  413.097    0.000 {built-in method _functools.reduce}
                2559018  235.629    0.000  399.610    0.000 collector.py:53(collect)
             2131829006  397.268    0.000  397.268    0.000 enum.py:352(<genexpr>)
              237317889  130.052    0.000  371.209    0.000 layers.py:565(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9507476: <MONTEST_CF_5c2_1> in cluster <dcc> Done

Job <MONTEST_CF_5c2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:49 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 10 03:32:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 10 03:32:59 2021
Terminated at Sun Apr 11 01:28:13 2021
Results reported at Sun Apr 11 01:28:13 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   78705.59 sec.
    Max Memory :                                 8377 MB
    Average Memory :                             5987.51 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8007.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78914 sec.
    Turnaround time :                            82284 sec.

The output (if any) is above this job summary.

