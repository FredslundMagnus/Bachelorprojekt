
# Parameters

    Name :                      Causal4_Conver4_3counterfacts-2
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      62171035897 function calls (61857580238 primitive calls) in 86110.10 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.102 86110.102 {built-in method builtins.exec}
                      1    4.571    4.571 86110.102 86110.102 <string>:1(<module>)
                      1  330.482  330.482 86105.531 86105.531 main.py:80(CFagent)
                2555691 2254.323    0.001 24112.464    0.009 agent.py:212(counterfact)
                7667073   34.586    0.000 19527.413    0.003 agent.py:29(learn)
                2555691   13.655    0.000 17333.023    0.007 game.py:42(step)
                2555691   17.307    0.000 16712.335    0.007 layers.py:827(step)
                7667069  491.954    0.000 15811.146    0.002 learner.py:42(Qlearn)
        348094098/34640130 1418.678    0.000 11466.995    0.000 module.py:866(_call_impl)
              101152565 11168.441    0.000 11168.441    0.000 {built-in method tensor}
               95197035   53.016    0.000 11045.827    0.000 game.py:38(board)
                2555691  259.396    0.000 10964.044    0.004 layers.py:17(step)
               26973061   73.663    0.000 10800.486    0.000 network.py:28(forward)
              255011896  793.074    0.000 10681.213    0.000 layer.py:106(move)
               26973061  367.785    0.000 10542.255    0.000 container.py:117(forward)
                2555691  310.278    0.000 7609.649    0.003 agent.py:54(_learn)
                2555691  301.851    0.000 6894.146    0.003 agent.py:204(_learn)
              255011896 1279.110    0.000 6503.055    0.000 layers.py:844(check)
                2555691 5597.909    0.002 6453.711    0.003 replaybuffer.py:22(sample_data)
              102227630 3615.294    0.000 6381.029    0.000 layer.py:159(update)
                9651812  279.625    0.000 6326.327    0.001 agent.py:49(__call__)
                4542802   88.768    0.000 6211.387    0.001 agent.py:176(choose_action)
                7667069   76.780    0.000 6119.823    0.001 optimizer.py:84(wrapper)
                2555691 5165.010    0.002 5970.396    0.002 replaybuffer.py:67(sample_data)
                7667069   41.115    0.000 5800.603    0.001 grad_mode.py:24(decorate_context)
                2555692  406.148    0.000 5706.098    0.002 layers.py:793(update)
                7667069  264.390    0.000 5673.301    0.001 adam.py:55(step)
                7667069 1185.967    0.000 5131.305    0.001 _functional.py:53(adam)
                2555691   84.501    0.000 4970.449    0.002 agent.py:117(_learn)
                7667069   34.232    0.000 4158.323    0.001 tensor.py:195(backward)
                7667069   35.558    0.000 4123.021    0.001 __init__.py:68(backward)
                7667069 3922.612    0.001 3922.612    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               53946122  122.063    0.000 3871.672    0.000 conv.py:398(forward)
                2555691 2223.079    0.001 3797.338    0.001 replaybuffer.py:28(teleporter_save_data)
               53946122   74.859    0.000 3690.715    0.000 conv.py:390(_conv_forward)
               53946122 3615.856    0.000 3615.856    0.000 {built-in method conv2d}
                2555691 1918.577    0.001 3594.007    0.001 agent.py:88(interveen)
               75807801  157.579    0.000 2988.632    0.000 linear.py:93(forward)
              255011896  512.295    0.000 2867.593    0.000 layers.py:838(isFree)
               75807801   62.782    0.000 2751.602    0.000 functional.py:1737(linear)
               75807801 2673.651    0.000 2673.651    0.000 {built-in method torch._C._nn.linear}
             2377411220 1963.560    0.000 2355.298    0.000 layer.py:103(isFree)
                2555691 1309.216    0.001 1983.187    0.001 agent.py:67(modify)
               12207503   80.411    0.000 1622.114    0.000 agent.py:59(modify_board)
              102780862   85.677    0.000 1573.077    0.000 activation.py:713(forward)
             1028452343 1523.975    0.000 1523.975    0.000 layer.py:154(elements)
              149023667 1496.504    0.000 1496.504    0.000 {built-in method clone}
              102780862   83.779    0.000 1487.400    0.000 functional.py:1364(leaky_relu)
               37764393 1448.041    0.000 1448.041    0.000 {built-in method cat}
             5138768627  945.972    0.000 1388.539    0.000 enum.py:646(__hash__)
              102780862 1386.037    0.000 1386.037    0.000 {built-in method torch._C._nn.leaky_relu}
                4542802 1076.151    0.000 1252.853    0.000 agent.py:187(convert_values)
              260278821  278.575    0.000 1218.698    0.000 {built-in method builtins.any}
                2957451   45.001    0.000 1202.155    0.000 layers.py:849(restart)
                2555687   52.835    0.000 1183.973    0.000 agent.py:172(__call__)
                2555691   50.595    0.000 1127.319    0.000 agent.py:112(__call__)
               12207503 1071.359    0.000 1071.359    0.000 {built-in method torch._C._nn.one_hot}
              255011896  789.488    0.000 1029.171    0.000 layers.py:77(check)
                2555691  809.925    0.000 1028.376    0.000 replaybuffer.py:73(CF_save_data)
              143118616 1002.519    0.000 1002.519    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              255011896  633.012    0.000  976.522    0.000 layers.py:286(check)
             2778729239  772.333    0.000  940.123    0.000 layers.py:809(<genexpr>)
              255569200  101.039    0.000  900.739    0.000 {built-in method builtins.all}
                7667069  165.330    0.000  899.957    0.000 optimizer.py:189(zero_grad)
              143118616  882.058    0.000  882.058    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2957451   18.756    0.000  864.870    0.000 level.py:8(__init__)
             1071866073  299.599    0.000  831.988    0.000 layers.py:799(<genexpr>)
              255011896  496.242    0.000  824.251    0.000 layers.py:246(check)
        12203086216/12203086213  742.124    0.000  812.156    0.000 {built-in method builtins.len}
                2957451  105.371    0.000  680.668    0.000 levels.py:199(generate)
                9651812  235.868    0.000  645.216    0.000 exploration.py:53(softmaxer)
                2555691   54.591    0.000  645.209    0.000 replaybuffer.py:18(stacker)
             6641669619  620.201    0.000  620.201    0.000 layer.py:99(positions)
                2555687   55.093    0.000  606.675    0.000 replaybuffer.py:63(stacker)
              255011896  462.503    0.000  595.812    0.000 layers.py:62(check)
               71559308  583.184    0.000  583.184    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               71559308  518.657    0.000  518.657    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              255569200  330.146    0.000  485.249    0.000 layers.py:113(isDone)
               71559308  481.719    0.000  481.719    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                5914902   54.987    0.000  473.990    0.000 level.py:41(notUsed)
               71559308  455.565    0.000  455.565    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               11026284  176.883    0.000  450.277    0.000 random.py:315(sample)
             5138797890  442.573    0.000  442.573    0.000 {built-in method builtins.hash}
              255011896  279.312    0.000  436.904    0.000 layers.py:273(check)
              255011896  274.045    0.000  433.627    0.000 layers.py:313(check)
              500915240  346.718    0.000  427.027    0.000 tensor.py:906(grad)
              102227630  412.532    0.000  412.532    0.000 layer.py:171(<listcomp>)
                2555691  234.726    0.000  400.835    0.000 collector.py:46(collect)
                7667069   13.627    0.000  367.458    0.000 loss.py:527(forward)
              255011896  249.784    0.000  367.160    0.000 layers.py:48(check)
                7667069   39.215    0.000  353.831    0.000 functional.py:2898(mse_loss)
               71559308  351.956    0.000  351.956    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              163786857  350.784    0.000  350.784    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              102227630  317.048    0.000  317.048    0.000 layer.py:172(<listcomp>)
              244916098  239.324    0.000  316.985    0.000 layer.py:134(remove)
              255011896  205.177    0.000  298.563    0.000 layers.py:23(check)
               29574510   41.874    0.000  282.279    0.000 layer.py:77(restart)
               53946122   39.526    0.000  259.345    0.000 flatten.py:39(forward)
              413018815  174.492    0.000  244.022    0.000 layer.py:138(add)
             2817116104  241.200    0.000  241.200    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618557: <Causal4_Conver4_3counterfacts_2> in cluster <dcc> Done

Job <Causal4_Conver4_3counterfacts_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 00:28:49 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May  6 06:34:15 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May  6 06:34:15 2021
Terminated at Fri May  7 06:29:29 2021
Results reported at Fri May  7 06:29:29 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85905.95 sec.
    Max Memory :                                 7998 MB
    Average Memory :                             5638.40 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8386.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86163 sec.
    Turnaround time :                            108040 sec.

The output (if any) is above this job summary.

