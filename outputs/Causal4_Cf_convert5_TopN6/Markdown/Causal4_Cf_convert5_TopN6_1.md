
# Parameters

    Name :                      Causal4_Cf_convert5_TopN6-1
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                5
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      79381387737 function calls (79029330466 primitive calls) in 86113.93 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.929 86113.929 {built-in method builtins.exec}
                      1    4.379    4.379 86113.929 86113.929 <string>:1(<module>)
                      1  402.443  402.443 86109.550 86109.550 main.py:79(CFagent)
               11499552   41.774    0.000 26437.972    0.002 agent.py:29(learn)
                3833184   15.209    0.000 22262.038    0.006 game.py:41(step)
               11499540  679.812    0.000 21477.388    0.002 learner.py:42(Qlearn)
                3833184   21.048    0.000 21400.440    0.006 layers.py:718(step)
                3833184  317.613    0.000 14346.680    0.004 layers.py:17(step)
              382863609 1043.146    0.000 13996.516    0.000 layer.py:98(move)
        394170813/42115233 1476.085    0.000 12146.007    0.000 module.py:866(_call_impl)
               30615693   81.577    0.000 11347.449    0.000 network.py:27(forward)
               30615693  367.574    0.000 11080.387    0.000 container.py:117(forward)
                3833184  841.344    0.000 10574.312    0.003 agent.py:210(counterfact)
                3833184  388.436    0.000 10281.158    0.003 agent.py:54(_learn)
                3833184  384.917    0.000 9425.864    0.002 agent.py:202(_learn)
              382863609 1712.488    0.000 8655.289    0.000 layers.py:735(check)
               11499540   93.004    0.000 8380.854    0.001 optimizer.py:84(wrapper)
               11499540   46.516    0.000 7968.442    0.001 grad_mode.py:24(decorate_context)
               11499540  322.410    0.000 7822.375    0.001 adam.py:55(step)
               11499540 1624.316    0.000 7134.779    0.001 _functional.py:53(adam)
                3833185  544.864    0.000 7001.584    0.002 layers.py:684(update)
                3833184  111.891    0.000 6667.018    0.002 agent.py:117(_learn)
                3833184 5493.086    0.001 6630.618    0.002 replaybuffer.py:22(sample_data)
                3833184 5302.888    0.001 6396.291    0.002 replaybuffer.py:67(sample_data)
               60144981 6049.446    0.000 6049.446    0.000 {built-in method tensor}
               51371605   29.022    0.000 5845.813    0.000 game.py:37(board)
                9542489  236.464    0.000 5807.253    0.001 agent.py:49(__call__)
               11499540   44.024    0.000 5524.272    0.000 tensor.py:195(backward)
               11499540   42.905    0.000 5478.711    0.000 __init__.py:68(backward)
               11499540 5220.302    0.000 5220.302    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               76663690 2667.171    0.000 4593.505    0.000 layer.py:151(update)
               61231386  128.782    0.000 4134.768    0.000 conv.py:398(forward)
               61231386   89.282    0.000 3944.553    0.000 conv.py:390(_conv_forward)
               61231386 3855.271    0.000 3855.271    0.000 {built-in method conv2d}
                3833184 1549.077    0.000 3849.517    0.001 agent.py:88(interveen)
              382863609  736.505    0.000 3593.885    0.000 layers.py:729(isFree)
               84180711  162.573    0.000 3126.632    0.000 linear.py:93(forward)
                3833184 1701.836    0.000 3024.591    0.001 replaybuffer.py:28(teleporter_save_data)
               84180711   65.501    0.000 2882.642    0.000 functional.py:1737(linear)
             3290396871 2382.422    0.000 2857.381    0.000 layer.py:95(isFree)
               84180711 2801.641    0.000 2801.641    0.000 {built-in method torch._C._nn.linear}
                3833184 1721.567    0.000 2627.797    0.001 agent.py:67(modify)
                1907308   38.152    0.000 2360.516    0.001 agent.py:175(choose_action)
               51707453 1855.426    0.000 1855.426    0.000 {built-in method cat}
             7467194981 1284.051    0.000 1846.601    0.000 enum.py:646(__hash__)
               13375673   81.242    0.000 1663.379    0.000 agent.py:59(modify_board)
              383685596  372.644    0.000 1648.249    0.000 {built-in method builtins.any}
              114796404   86.668    0.000 1645.963    0.000 activation.py:713(forward)
                3833172   63.472    0.000 1621.789    0.000 agent.py:171(__call__)
              114796404   91.114    0.000 1559.296    0.000 functional.py:1364(leaky_relu)
                3833184   59.062    0.000 1529.542    0.000 agent.py:112(__call__)
              114796404 1450.427    0.000 1450.427    0.000 {built-in method torch._C._nn.leaky_relu}
              214658064 1402.530    0.000 1402.530    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              382863609 1049.123    0.000 1390.258    0.000 layers.py:77(check)
              139136918 1334.093    0.000 1334.093    0.000 {built-in method clone}
             4178376521 1047.679    0.000 1275.605    0.000 layers.py:700(<genexpr>)
              382863609  817.382    0.000 1259.409    0.000 layers.py:286(check)
               11499540  219.445    0.000 1248.356    0.000 optimizer.py:189(zero_grad)
              214658064 1241.719    0.000 1241.719    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3466089   40.736    0.000 1208.424    0.000 layers.py:740(restart)
                3833184  944.805    0.000 1189.329    0.000 replaybuffer.py:73(CF_save_data)
              382863609  680.186    0.000 1108.368    0.000 layers.py:246(check)
               13375673 1098.117    0.000 1098.117    0.000 {built-in method torch._C._nn.one_hot}
             1226804692 1071.449    0.000 1071.449    0.000 layer.py:146(elements)
              383318500  100.899    0.000 1020.491    0.000 {built-in method builtins.all}
             1168581082  278.969    0.000  964.818    0.000 layers.py:690(<genexpr>)
                3833184   68.570    0.000  870.923    0.000 replaybuffer.py:18(stacker)
             9829956595  867.101    0.000  867.101    0.000 layer.py:91(positions)
                3466089   20.051    0.000  856.644    0.000 level.py:8(__init__)
                3833172   68.411    0.000  835.170    0.000 replaybuffer.py:63(stacker)
              107329032  825.156    0.000  825.156    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              382863609  587.590    0.000  762.964    0.000 layers.py:62(check)
              107329032  706.218    0.000  706.218    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        10167838574/10167838571  619.530    0.000  687.822    0.000 {built-in method builtins.len}
                3466089  114.138    0.000  687.072    0.000 levels.py:199(generate)
              107329032  659.659    0.000  659.659    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              383318500  433.159    0.000  654.524    0.000 layers.py:113(isDone)
              107329032  648.803    0.000  648.803    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              382863609  379.636    0.000  600.643    0.000 layers.py:273(check)
              382863609  366.542    0.000  579.781    0.000 layers.py:313(check)
              751303308  459.290    0.000  573.963    0.000 tensor.py:906(grad)
                9542489  213.388    0.000  572.388    0.000 exploration.py:53(softmaxer)
             7467238580  562.557    0.000  562.557    0.000 {built-in method builtins.hash}
               14598546  215.416    0.000  562.208    0.000 random.py:315(sample)
                3833184  327.742    0.000  557.570    0.000 collector.py:46(collect)
              382863609  344.347    0.000  509.440    0.000 layers.py:48(check)
              107329032  504.618    0.000  504.618    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11499540   17.858    0.000  467.926    0.000 loss.py:527(forward)
                6932178   54.625    0.000  466.517    0.000 level.py:41(notUsed)
               11499540   41.854    0.000  450.068    0.000 functional.py:2898(mse_loss)
              382863609  263.232    0.000  390.533    0.000 layers.py:23(check)
                1907308  356.054    0.000  378.431    0.000 agent.py:186(convert_values)
             4226185941  312.088    0.000  312.088    0.000 {method 'random' of '_random.Random' objects}
              156345763  310.850    0.000  310.850    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               34660890   44.186    0.000  300.223    0.000 layer.py:69(restart)
              328857227  212.260    0.000  298.279    0.000 layer.py:126(remove)
              537383854  211.998    0.000  287.542    0.000 layer.py:130(add)
               11499540  279.025    0.000  279.025    0.000 {built-in method torch._C._nn.mse_loss}
                7666370  276.623    0.000  276.623    0.000 {built-in method nonzero}
               76663690  276.478    0.000  276.478    0.000 layer.py:163(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533968: <Causal4_Cf_convert5_TopN6_1> in cluster <dcc> Done

Job <Causal4_Cf_convert5_TopN6_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 21 01:50:06 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 01:50:06 2021
Terminated at Thu Apr 22 01:45:28 2021
Results reported at Thu Apr 22 01:45:28 2021

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

    CPU time :                                   85906.20 sec.
    Max Memory :                                 10806 MB
    Average Memory :                             6998.39 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5578.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86123 sec.
    Turnaround time :                            278720 sec.

The output (if any) is above this job summary.

