
# Parameters

    Name :                      SuperCausal_convert4-1
    Main :                      CFagent
    Level :                     Levels.CausalSuper
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
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
    Counterfacts :              2
    Topn :                      3
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      79275497440 function calls (78994574029 primitive calls) in 86119.08 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86119.083 86119.083 {built-in method builtins.exec}
                      1    4.213    4.213 86119.083 86119.083 <string>:1(<module>)
                      1  329.016  329.016 86114.870 86114.870 main.py:80(CFagent)
                8958219   35.926    0.000 26975.098    0.003 agent.py:29(learn)
                8958219  675.188    0.000 22456.826    0.003 learner.py:42(Qlearn)
                2986073   13.488    0.000 19183.750    0.006 game.py:42(step)
                2986073   18.605    0.000 18437.926    0.006 layers.py:827(step)
                2986073  934.283    0.000 14439.827    0.005 agent.py:212(counterfact)
                2986073  256.496    0.000 13386.913    0.004 layers.py:17(step)
              298365981  489.795    0.000 13104.170    0.000 layer.py:106(move)
        314285440/33363720 1309.500    0.000 11673.468    0.000 module.py:866(_call_impl)
               24405501   71.623    0.000 10954.538    0.000 network.py:28(forward)
               24405501  337.720    0.000 10728.969    0.000 container.py:117(forward)
                2986073  316.325    0.000 10418.823    0.003 agent.py:54(_learn)
              298365981 1306.601    0.000 9710.271    0.000 layers.py:844(check)
                2986073  313.875    0.000 9640.988    0.003 agent.py:204(_learn)
                8958219   80.703    0.000 9513.098    0.001 optimizer.py:84(wrapper)
                8958219   38.972    0.000 9143.112    0.001 grad_mode.py:24(decorate_context)
                8958219  263.493    0.000 9018.701    0.001 adam.py:55(step)
                8958219 1852.752    0.000 8461.700    0.001 _functional.py:53(adam)
               77196138 8431.445    0.000 8431.445    0.000 {built-in method tensor}
               70289971   43.739    0.000 8243.858    0.000 game.py:38(board)
                2986073   91.558    0.000 6859.305    0.002 agent.py:117(_learn)
                7719613  208.318    0.000 5625.508    0.001 agent.py:49(__call__)
                8958219   37.340    0.000 5582.611    0.001 tensor.py:195(backward)
                8958219   34.541    0.000 5543.950    0.001 __init__.py:68(backward)
                8958219 5307.386    0.001 5307.386    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2986073 4162.185    0.001 5182.552    0.002 replaybuffer.py:22(sample_data)
                2986073 4116.499    0.001 5096.558    0.002 replaybuffer.py:67(sample_data)
                2986074  418.163    0.000 5008.793    0.002 layers.py:793(update)
               89582190 2411.400    0.000 4529.536    0.000 layer.py:175(NoRock_update)
                2986073 2416.646    0.001 4492.261    0.002 replaybuffer.py:28(teleporter_save_data)
                2986073 2275.605    0.001 4442.213    0.001 agent.py:88(interveen)
               48811002  106.481    0.000 3862.330    0.000 conv.py:398(forward)
               48811002   67.575    0.000 3706.435    0.000 conv.py:390(_conv_forward)
               48811002 3638.860    0.000 3638.860    0.000 {built-in method conv2d}
               67244357  150.881    0.000 3109.915    0.000 linear.py:93(forward)
               67244357   55.628    0.000 2893.393    0.000 functional.py:1737(linear)
               67244357 2824.392    0.000 2824.392    0.000 {built-in method torch._C._nn.linear}
                1755523   38.191    0.000 2708.905    0.002 agent.py:176(choose_action)
                2986073 1655.332    0.001 2526.684    0.001 agent.py:67(modify)
              298365981  571.181    0.000 2466.137    0.000 layers.py:838(isFree)
            10870343877 1677.258    0.000 2429.270    0.000 enum.py:646(__hash__)
              298365981 1216.284    0.000 1972.241    0.000 layers.py:734(check)
             2948452619 1560.286    0.000 1894.955    0.000 layer.py:103(isFree)
              142569296 1843.639    0.000 1843.639    0.000 {built-in method clone}
              167220088 1742.595    0.000 1742.595    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               40566416 1740.719    0.000 1740.719    0.000 {built-in method cat}
               91649858   79.820    0.000 1729.351    0.000 activation.py:713(forward)
               91649858   73.262    0.000 1649.531    0.000 functional.py:1364(leaky_relu)
              298365981 1019.783    0.000 1633.526    0.000 layers.py:700(check)
               10705686   76.428    0.000 1562.684    0.000 agent.py:59(modify_board)
               91649858 1560.633    0.000 1560.633    0.000 {built-in method torch._C._nn.leaky_relu}
              298365981  927.725    0.000 1518.199    0.000 layers.py:717(check)
              167220088 1515.402    0.000 1515.402    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2986073   55.047    0.000 1513.859    0.001 agent.py:172(__call__)
                2986073   51.752    0.000 1429.915    0.000 agent.py:112(__call__)
                8958219  212.573    0.000 1311.266    0.000 optimizer.py:189(zero_grad)
              303159070  290.559    0.000 1293.363    0.000 {built-in method builtins.any}
              819004643 1130.556    0.000 1130.556    0.000 layer.py:154(elements)
             3269056164  821.487    0.000 1002.804    0.000 layers.py:809(<genexpr>)
               10705686  993.311    0.000  993.311    0.000 {built-in method torch._C._nn.one_hot}
            10079612235  950.090    0.000  950.090    0.000 layer.py:99(positions)
               83610044  946.891    0.000  946.891    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1420476   17.573    0.000  910.021    0.001 layers.py:849(restart)
                2986073  707.291    0.000  858.742    0.000 replaybuffer.py:73(CF_save_data)
              298365981  555.897    0.000  852.987    0.000 layers.py:686(check)
               83610044  810.726    0.000  810.726    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2986073   63.793    0.000  806.366    0.000 replaybuffer.py:18(stacker)
               83610044  787.288    0.000  787.288    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1420476    8.390    0.000  784.427    0.001 level.py:8(__init__)
               83610044  781.771    0.000  781.771    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2986073   66.798    0.000  774.077    0.000 replaybuffer.py:63(stacker)
              298365981  468.698    0.000  752.063    0.000 layers.py:672(check)
            10870377956  752.018    0.000  752.018    0.000 {built-in method builtins.hash}
              298365981  464.797    0.000  747.976    0.000 layers.py:658(check)
              298607400  109.274    0.000  717.142    0.000 {built-in method builtins.all}
        11036697173/11036697170  648.054    0.000  714.925    0.000 {built-in method builtins.len}
                1420476   25.818    0.000  704.312    0.000 levels.py:261(generate)
               11660753  107.940    0.000  651.724    0.000 level.py:41(notUsed)
             1252254761  323.850    0.000  642.930    0.000 layers.py:799(<genexpr>)
                2986073  371.944    0.000  617.769    0.000 collector.py:46(collect)
               83610044  602.405    0.000  602.405    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7719613  213.595    0.000  585.096    0.000 exploration.py:53(softmaxer)
                1755523  456.872    0.000  540.913    0.000 agent.py:187(convert_values)
              585270392  387.811    0.000  481.517    0.000 tensor.py:906(grad)
              156261055  476.626    0.000  476.626    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                8958219   12.116    0.000  438.224    0.000 loss.py:527(forward)
                8958219   34.555    0.000  426.108    0.000 functional.py:2898(mse_loss)
                5972146  153.821    0.000  409.070    0.000 random.py:315(sample)
              298365981  229.500    0.000  351.322    0.000 layers.py:646(check)
               11660753    9.552    0.000  313.853    0.000 level.py:38(elementsIn)
               89582190  308.399    0.000  308.399    0.000 layer.py:186(<listcomp>)
              298365981  197.751    0.000  297.757    0.000 layers.py:23(check)
               48811002   37.635    0.000  286.070    0.000 flatten.py:39(forward)
             2948452619  284.351    0.000  284.351    0.000 layer.py:211(isBlocking)
                8958219  280.123    0.000  280.123    0.000 {built-in method torch._C._nn.mse_loss}
               17916438  261.754    0.000  261.754    0.000 {built-in method sum}
               89582190  256.919    0.000  256.919    0.000 layer.py:187(<listcomp>)
                5972148  255.190    0.000  255.190    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9672993: <SuperCausal_convert4_1> in cluster <dcc> Done

Job <SuperCausal_convert4_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May 20 18:43:27 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri May 21 18:38:55 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri May 21 18:38:55 2021
Terminated at Sat May 22 18:34:33 2021
Results reported at Sat May 22 18:34:33 2021

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

    CPU time :                                   85895.51 sec.
    Max Memory :                                 8820 MB
    Average Memory :                             5944.97 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7564.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86139 sec.
    Turnaround time :                            172266 sec.

The output (if any) is above this job summary.

